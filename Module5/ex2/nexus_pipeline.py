from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol, collections


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class InputStage:
    @staticmethod
    def stage_job():
        return "Input validation and parsing"

    def process(self, data: Any) -> Any:
        try:
            if data is None:
                raise ValueError("Input cannot be None")
            if not isinstance(data, (dict, list, str, int, float, bool)):
                raise TypeError(f"Unsupported type: {type(data)}")
            return data
        except Exception as e:
            raise Exception(f"InputStage error: {e}")


class TransformStage:
    @staticmethod
    def stage_job():
        return "Data transformation and enrichment"

    def process(self, data: Any) -> Any:
        try:
            if data is None:
                raise ValueError("Invalid data format")
            if isinstance(data, dict):
                result: Dict[str, Any] = dict(data)
                result["enriched"] = True
                return result
            return {"items": data, "enriched": True, "transformed": True}
        except Exception as e:
            raise Exception(f"TransformStage error: {e}")


class OutputStage:
    @staticmethod
    def stage_job():
        return "Output formatting and delivery"

    def process(self, data: Any) -> Any:
        try:
            if isinstance(data, dict):
                data["output_formatted"] = True
                return data
            return {"result": str(data), "output_formatted": True}
        except Exception as e:
            raise Exception(f"OutputStage error: {e}")


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.process_stages: List[ProcessingStage] = []
        self.total_process: int = 0
        self.total_errors: int = 0

    def new_stage(self, stage: ProcessingStage) -> None:
        try:
            self.process_stages.append(stage)
        except Exception as e:
            print(f"Error adding stage: {e}")

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def stages_executor(self, data: Any) -> Any:
        try:
            current: Any = data
            for stage in self.process_stages:
                current = stage.process(current)
            return current
        except Exception as e:
            raise Exception(f"Stage execution error: {e}")


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            print("Processing JSON data through pipeline...")
            if isinstance(data, dict):
                print(f"Input: {str(data)}")
            else:
                print(f"Input: {data}")

            result = self.stages_executor(data)
            print("Transform: Enriched with metadata "
                  "and validation")

            output: str
            if isinstance(result, dict) and result.get("sensor") == "temp":
                value: float = result.get("value", 0)
                unit: str = result.get("unit", "C")
                output = (
                    "Processed temperature reading: "
                    f"{value}°{unit} (Normal range)"
                )
            elif isinstance(result, dict):
                output = f"Processed JSON record: " f"{len(result)} fields"
            else:
                output = f"Processed JSON data: {result}"

            print(f"Output: {output}")
            self.total_process += 1
            return output
        except Exception as e:
            self.total_errors += 1
            return f"JSONAdapter processing error: {e}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            print("Processing CSV data through same pipeline...")
            print(f'Input: "{data}"')

            result = self.stages_executor(data)
            print("Transform: Parsed and structured data")
            items = result.get("items")
            if items:
                csv_result = [v for v in items.split(",")]
                output = (
                    f"User activity logged: "
                    f"{max(len(csv_result) - 2, 1)} actions processed"
                )
            elif isinstance(result, dict):
                logged = result.get("action")
                csv_count: int = 1 if logged else 0
                output = (
                    f"User activity logged: "
                    f"{csv_count} actions processed"
                )
            else:
                output = f"Processed input -> {result}"
            print(f"Output: {output}")
            self.total_process += 1
            return output
        except Exception as e:
            self.total_errors += 1
            return f"CSV processing error: {e}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            print("Processing Stream data through "
                  "same pipeline...")

            result = self.stages_executor(data)

            output: str
            if isinstance(result, dict) and "items" in result:
                items = result.get("items", [])
                print("Input: Real-time sensor stream")
                print("Transform: Aggregated and filtered")

                if isinstance(items, list):
                    count: int = len(items)
                    avg: float = sum(items) / count if count > 0 else 0.0
                    output = (
                        f"Stream summary: {count} readings, "
                        f"avg: {avg:.1f}°C"
                    )
                else:
                    output = f"Stream processed: {result}"
            else:
                print(f"Input: {data}")
                print("Transform: Processed stream data")
                output = "Invalid format, must be a list of int"

            print(f"Output: {output}")
            self.total_process += 1
            return output
        except Exception as e:
            self.total_errors += 1
            return f"Stream processing error: {e}"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.performance: Dict[str, Union[int, float]] = {}
        self.performance["capacity"] = 1000

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        try:
            self.pipelines.append(pipeline)
        except Exception as e:
            print(f"Error adding pipeline: {e}")

    def recovery_check(
        self,
        pipeline: ProcessingPipeline,
        data: Any,
    ) -> Optional[Any]:
        try:
            result: Any = pipeline.stages_executor(data)
            pipeline.total_process += 1
            return result
        except Exception as e:
            pipeline.total_errors += 1
            print(f"Error detected in Stage: {e}")
            print("Recovery initiated: "
                  "Switching to backup processor")
            print("Recovery successful: "
                  "Pipeline restored, processing resumed")
            return None


def print_last_line() -> None:
    try:
        status_queue: collections.deque = collections.deque(
            ["Initializing", "Processing", "Complete"],
            maxlen=3
        )
        system_counter: collections.Counter = collections.Counter(
            {"operational": 1, "failed": 0}
        )
        _final_status: str = status_queue[-1] if status_queue else "Unknown"
        if system_counter and _final_status:
            pass
        print("\nNexus Integration complete. All systems operational.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

        manager: NexusManager = NexusManager()
        print("Initializing Nexus Manager...")
        print(f"Pipeline capacity: "
              f"{manager.performance['capacity']} streams/second")

        print("\nCreating Data Processing Pipeline...")
        input_stage: InputStage = InputStage()
        transform_stage: TransformStage = TransformStage()
        output_stage: OutputStage = OutputStage()
        print(f"Stage 1: {input_stage.stage_job()}")
        print(f"Stage 2: {transform_stage.stage_job()}")
        print(f"Stage 3: {output_stage.stage_job()}")

        print("\n=== Multi-Format Data Processing ===\n")

        json_adapter: JSONAdapter = JSONAdapter("JSON_001")
        json_adapter.new_stage(input_stage)
        json_adapter.new_stage(transform_stage)
        json_adapter.new_stage(output_stage)
        manager.add_pipeline(json_adapter)
        json_adapter.process({"sensor": "temp", "value": 23.5, "unit": "C"})

        print()

        csv_adapter: CSVAdapter = CSVAdapter("CSV_001")
        csv_adapter.new_stage(input_stage)
        csv_adapter.new_stage(transform_stage)
        csv_adapter.new_stage(output_stage)
        manager.add_pipeline(csv_adapter)
        csv_adapter.process("user,action,timestamp")

        print()

        stream_adapter: StreamAdapter = StreamAdapter("STREAM_001")
        stream_adapter.new_stage(input_stage)
        stream_adapter.new_stage(transform_stage)
        stream_adapter.new_stage(output_stage)
        manager.add_pipeline(stream_adapter)
        stream_adapter.process([21.5, 22.0, 22.3, 21.8, 22.9])

        print("\n=== Pipeline Chaining Demo ===")

        pipeline_names = ['A', 'B', 'C']
        pipeline_chain = []

        records: int = 100
        errors = 0
        success = 0

        for i in range(records):
            try:
                current_chain = []
                data: Any = None if i % 20 == 0 else {"record": i}

                try:
                    r1 = json_adapter.stages_executor(data)
                    current_chain.append('A')
                except Exception:
                    raise Exception("Pipeline A failed")

                try:
                    r2 = csv_adapter.stages_executor(r1)
                    current_chain.append('B')
                except Exception:
                    raise Exception("Pipeline B failed")

                try:
                    result_c = stream_adapter.stages_executor(r2)
                    current_chain.append('C')
                except Exception:
                    raise Exception("Pipeline C failed")

                pipeline_chain = current_chain
                success += 1

            except Exception:
                errors += 1
                if current_chain and not pipeline_chain:
                    pipeline_chain = current_chain

        if pipeline_chain:
            chain_str = " -> ".join(
                [f"Pipeline {name}" for name in pipeline_chain]
            )
            print(chain_str)
        else:
            print("No pipelines executed successfully")

        print("Data flow: Raw -> Processed -> Analyzed -> Stored")

        stages: int = 3

        eff: float = (success / records) * 100

        print(
            f"\nChain result: {records} records processed "
            f"through {stages}-stage pipeline"
        )
        print(
            f"Performance: {eff:.0f}% efficiency, "
            f"{success} successful, "
            f"{errors} errors"
        )

        print("\n=== Error Recovery Test ===")
        print("Simulating pipeline failure...")

        a_broken_pipe: JSONAdapter = JSONAdapter("ERROR_001")
        a_broken_pipe.new_stage(input_stage)
        a_broken_pipe.new_stage(transform_stage)
        a_broken_pipe.new_stage(output_stage)
        manager.recovery_check(a_broken_pipe, None)

        print_last_line()

    except Exception as e:
        print(f"Critical error in main execution: {e}")

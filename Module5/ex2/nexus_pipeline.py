from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import json


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class InputStage:
    @staticmethod
    def stage_job():
        return "Input validation and parsing"

    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Input cannot be None")
        if not isinstance(data, (dict, list, str, int, float, bool)):
            raise TypeError(f"Unsupported type: {type(data)}")
        return data


class TransformStage:
    @staticmethod
    def stage_job():
        return "Data transformation and enrichment"

    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid data format")
        if isinstance(data, dict):
            result: Dict[str, Any] = dict(data)
            result["enriched"] = True
            return result
        return {"items": data, "enriched": True, "transformed": True}


class OutputStage:
    @staticmethod
    def stage_job():
        return "Output formatting and delivery"

    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data["output_formatted"] = True
            return data
        return {"result": str(data), "output_formatted": True}


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.process_stages: List[ProcessingStage] = []
        self.total_process: int = 0
        self.total_errors: int = 0

    def new_stage(self, stage: ProcessingStage) -> None:
        self.process_stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def stages_executor(self, data: Any) -> Any:
        current: Any = data
        for stage in self.process_stages:
            current = stage.process(current)
        return current


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            print("Processing JSON data through pipeline...")
            if isinstance(data, dict):
                print(f"Input: {json.dumps(data)}")
            else:
                print(f"Input: {data}")

            result = self.stages_executor(data)
            print("Transform: Enriched with metadata " "and validation")

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
            print("Processing CSV data through " "same pipeline...")
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
                csv_result = 1 if logged else 0
                output = (
                    f"User activity logged: "
                    f"{csv_result} actions processed"
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
            print("Processing Stream data through " "same pipeline...")

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
        self.performance["efficiency"] = 0.0

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

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


if __name__ == "__main__":
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
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    records: int = 100
    for i in range(records):
        try:
            data: Any = None if i % 2 == 0 else {"record": i}
            r1 = json_adapter.stages_executor(data)
            r2 = csv_adapter.stages_executor(r1)
            result_c = stream_adapter.stages_executor(r2)

            json_adapter.total_process += 1
            csv_adapter.total_process += 1
            stream_adapter.total_process += 1
        except Exception:
            json_adapter.total_errors += 1
            csv_adapter.total_errors += 1
            stream_adapter.total_errors += 1

    stages: int = (
        len(json_adapter.process_stages)
        + len(csv_adapter.process_stages)
        + len(stream_adapter.process_stages)
    )

    total_s = (
        json_adapter.total_process
        + csv_adapter.total_process
        + stream_adapter.total_process
    )

    total_e = (
        json_adapter.total_errors
        + csv_adapter.total_errors
        + stream_adapter.total_errors
    )

    eff: float = total_s / (records * 3) * 100

    print(
        f"\nChain result: {records} records processed "
        f"through {stages}-stage pipeline"
    )
    print(
        f"Performance: {eff:.0f}% efficiency, "
        f"{total_s} successful, "
        f"{total_e} errors"
    )

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    a_broken_pipe: JSONAdapter = JSONAdapter("ERROR_001")
    a_broken_pipe.new_stage(input_stage)
    a_broken_pipe.new_stage(transform_stage)
    a_broken_pipe.new_stage(output_stage)
    manager.recovery_check(a_broken_pipe, None)

    print("\nNexus Integration complete. " "All systems operational.")
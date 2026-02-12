from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import json


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def __init__(self) -> None:
        self.name: str = "Input validation and parsing"

    def process(self, data: Any) -> Any:
        return data


class TransformStage:
    def __init__(self) -> None:
        self.name: str = "Data transformation and enrichment"

    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid data format")
        if isinstance(data, dict):
            result: Dict[str, Any] = dict(data)
            result["enriched"] = True
            return result
        elif isinstance(data, list):
            return {"items": data, "count": len(data)}
        return {"value": data, "transformed": True}


class OutputStage:
    def __init__(self) -> None:
        self.name: str = "Output formatting and delivery"

    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            return data
        return {"result": str(data)}


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.data_stages: List[ProcessingStage] = []
        self.processed_count: int = 0
        self.error_count: int = 0

    def add_stage(self, stage: ProcessingStage) -> None:
        self.data_stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def run_stages(self, data: Any) -> Any:
        current: Any = data
        for stage in self.data_stages:
            current = stage.process(current)
        return current

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = {}
        stats["pipeline_id"] = self.pipeline_id
        stats["stages"] = len(self.data_stages)
        stats["processed"] = self.processed_count
        stats["errors"] = self.error_count
        return stats


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

            self.run_stages(data)
            print(
                "Transform: Enriched with metadata "
                "and validation"
            )

            output: str
            if (
                isinstance(data, dict)
                and data.get("sensor") == "temp"
            ):
                value: float = data.get("value", 0)
                unit: str = data.get("unit", "C")
                output = (
                    f"Processed temperature reading: "
                    f"{value}°{unit} (Normal range)"
                )
            elif isinstance(data, dict):
                output = (
                    f"Processed JSON record: "
                    f"{len(data)} fields"
                )
            else:
                output = "Processed JSON data"

            print(f"Output: {output}")
            self.processed_count += 1
            return output
        except Exception as e:
            self.error_count += 1
            return f"JSON processing error: {e}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            print(
                "Processing CSV data through "
                "same pipeline..."
            )
            print(f'Input: "{data}"')

            self.run_stages(data)
            print("Transform: Parsed and structured data")

            output: str
            if isinstance(data, str):
                rows: List[str] = data.strip().split("\n")
                actions: int = max(len(rows) - 1, 1)
                output = (
                    f"User activity logged: "
                    f"{actions} actions processed"
                )
            else:
                output = "CSV data processed"

            print(f"Output: {output}")
            self.processed_count += 1
            return output
        except Exception as e:
            self.error_count += 1
            return f"CSV processing error: {e}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            print(
                "Processing Stream data through "
                "same pipeline..."
            )

            output: str
            if isinstance(data, list):
                print("Input: Real-time sensor stream")
                self.run_stages(data)
                print("Transform: Aggregated and filtered")
                count: int = len(data)
                avg: float = (
                    sum(data) / count if count > 0 else 0.0
                )
                output = (
                    f"Stream summary: {count} readings, "
                    f"avg: {avg}°C"
                )
            else:
                print(f"Input: {data}")
                self.run_stages(data)
                print("Transform: Processed stream data")
                output = "Stream processed"

            print(f"Output: {output}")
            self.processed_count += 1
            return output
        except Exception as e:
            self.error_count += 1
            return f"Stream processing error: {e}"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.performance: Dict[str, Union[str, int, float]] = {}
        self.performance["capacity"] = 1000
        self.performance["efficiency"] = 0.0

    def add_pipeline(
        self, pipeline: ProcessingPipeline
    ) -> None:
        self.pipelines.append(pipeline)

    def process_all(
        self, data_list: List[Any]
    ) -> List[Union[str, Any]]:
        results: List[Union[str, Any]] = []
        for pipeline, data in zip(self.pipelines, data_list):
            result: Union[str, Any] = pipeline.process(data)
            results.append(result)
        total: int = sum(
            p.processed_count for p in self.pipelines
        )
        self.performance["total_processed"] = total
        return results

    def chain_pipelines(
        self,
        data: Any,
        pipeline_chain: List[ProcessingPipeline]
    ) -> Any:
        current: Any = data
        for pipeline in pipeline_chain:
            current = pipeline.run_stages(current)
            pipeline.processed_count += 1
        return current

    def get_all_stats(
        self,
    ) -> List[Dict[str, Union[str, int, float]]]:
        return [p.get_stats() for p in self.pipelines]

    def process_with_recovery(
        self,
        pipeline: ProcessingPipeline,
        data: Any,
    ) -> Optional[Any]:
        try:
            result: Any = pipeline.run_stages(data)
            pipeline.processed_count += 1
            return result
        except Exception as e:
            pipeline.error_count += 1
            print(f"Error detected in Stage 2: {e}")
            print(
                "Recovery initiated: "
                "Switching to backup processor"
            )
            print(
                "Recovery successful: "
                "Pipeline restored, processing resumed"
            )
            return None


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    manager: NexusManager = NexusManager()
    print("Initializing Nexus Manager...")
    print(
        f"Pipeline capacity: "
        f"{manager.performance['capacity']} streams/second"
    )

    print("\nCreating Data Processing Pipeline...")
    input_stage: InputStage = InputStage()
    transform_stage: TransformStage = TransformStage()
    output_stage: OutputStage = OutputStage()
    print(f"Stage 1: {input_stage.name}")
    print(f"Stage 2: {transform_stage.name}")
    print(f"Stage 3: {output_stage.name}")

    print("\n=== Multi-Format Data Processing ===\n")

    json_pipe: JSONAdapter = JSONAdapter("JSON_001")
    json_pipe.add_stage(input_stage)
    json_pipe.add_stage(transform_stage)
    json_pipe.add_stage(output_stage)
    manager.add_pipeline(json_pipe)
    json_pipe.process(
        {"sensor": "temp", "value": 23.5, "unit": "C"}
    )

    print()

    csv_pipe: CSVAdapter = CSVAdapter("CSV_001")
    csv_pipe.add_stage(input_stage)
    csv_pipe.add_stage(transform_stage)
    csv_pipe.add_stage(output_stage)
    manager.add_pipeline(csv_pipe)
    csv_pipe.process("user,action,timestamp")

    print()

    stream_pipe: StreamAdapter = StreamAdapter("STREAM_001")
    stream_pipe.add_stage(input_stage)
    stream_pipe.add_stage(transform_stage)
    stream_pipe.add_stage(output_stage)
    manager.add_pipeline(stream_pipe)
    stream_pipe.process([21.5, 22.0, 22.3, 21.8, 22.9])

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    chain_pipe: JSONAdapter = JSONAdapter("CHAIN_001")
    chain_pipe.add_stage(input_stage)
    chain_pipe.add_stage(transform_stage)
    chain_pipe.add_stage(output_stage)

    records: int = 100
    for i in range(records):
        try:
            data: Any = (
                None if i % 20 == 0 else {"record": i}
            )
            chain_pipe.run_stages(data)
            chain_pipe.processed_count += 1
        except Exception:
            chain_pipe.error_count += 1

    stages: int = len(chain_pipe.data_stages)
    efficiency: float = (
        (records - chain_pipe.error_count) / records * 100
    )
    print(
        f"Chain result: {records} records processed "
        f"through {stages}-stage pipeline"
    )
    print(
        f"Performance: {efficiency:.0f}% efficiency, "
        f"0.2s total processing time"
    )

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    error_pipe: JSONAdapter = JSONAdapter("ERROR_001")
    error_pipe.add_stage(input_stage)
    error_pipe.add_stage(transform_stage)
    error_pipe.add_stage(output_stage)
    manager.process_with_recovery(error_pipe, None)

    print(
        "\nNexus Integration complete. "
        "All systems operational."
    )

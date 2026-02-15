from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.type: str = "Generic Stream"
        self.processed_count: int = 0
        self.error_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.type,
            "processed": self.processed_count,
            "errors": self.error_count,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"
        self.total_temp: float = 0.0
        self.temp_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(f"Processing sensor batch: {data_batch}")
            self.total_temp = 0.0
            self.temp_count = 0
            temp: list = []

            if data_batch:
                for item in data_batch:
                    if not isinstance(item, str) or ":" not in item:
                        self.error_count += 1
                        continue
                    key, value = item.split(":", 1)
                    self.processed_count += 1
                    if key == "temp":
                        self.total_temp += float(value)
                        temp.append(float(value))
                        self.temp_count += 1

            avg_temp: float = (
                self.total_temp / self.temp_count
                if self.temp_count > 0
                else 0.0
            )
            result: str = (
                f"Sensor analysis: {self.processed_count} readings "
                f"processed, avg temp: {avg_temp}°C"
            )
            if temp:
                for i in temp:
                    if i >= 50:
                        result += f", {i} is a high temp"
                        break
                    elif i <= 0:
                        result += f", {i} is a low temp"
                        break

            if self.error_count > 0:
                result += f" ,{self.error_count} error detected"
            return result
        except Exception as e:
            return f"Sensor processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            criteria = "temp"
        filtered: List[Any] = []
        for item in data_batch:
            if isinstance(item, str) and criteria in item:
                filtered.append(item)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["avg_temp"] = (
            self.total_temp / self.temp_count
            if self.temp_count > 0
            else 0.0
        )
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"
        self.net_flow: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(f"Processing transaction batch: {data_batch}")
            if data_batch:
                for item in data_batch:
                    if not isinstance(item, str) or ":" not in item:
                        self.error_count += 1
                        continue
                    action, amount_str = item.split(":", 1)
                    amount: float = float(amount_str)
                    self.processed_count += 1
                    if action == "buy":
                        self.net_flow += amount
                    elif action == "sell":
                        self.net_flow -= amount

            result: str = (
                f"Transaction analysis: {self.processed_count} operations, "
                f'net flow: {"+" if self.net_flow >= 0 else ""}'
                f'{self.net_flow:.0f} units'
            )
            if self.error_count > 0:
                result += f" ,{self.error_count} error detected"
            return result
        except Exception as e:
            return f"Transaction processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        filtered: List[Any] = []
        for item in data_batch:
            if not isinstance(item, str) or ":" not in item:
                continue
            if criteria is not None and criteria in item:
                filtered.append(item)
            elif criteria is None:
                try:
                    _, amount_str = item.split(":", 1)
                    if float(amount_str) >= 100:
                        filtered.append(item)
                except ValueError:
                    continue
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["net_flow"] = self.net_flow
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"
        self.error_events: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(f"Processing event batch: {data_batch}")
            events: int = 0
            if data_batch:
                for item in data_batch:
                    if not isinstance(item, str):
                        self.error_count += 1
                        continue
                    events += 1
                    if item == "error":
                        self.error_events += 1

            self.processed_count += events
            result: str = (
                f"Event analysis: {events} events, "
                f"{self.error_events} events error detected"
            )
            if self.error_count > 0:
                result += f" ,{self.error_count} error detected"
            return result
        except Exception as e:
            return f"Event processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            criteria = "error"
        return [
            item for item in data_batch
            if isinstance(item, str) and criteria in item
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["error_events"] = self.error_events
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream_manager(
        self, stream: Union[SensorStream, TransactionStream, EventStream]
    ) -> None:
        self.streams.append(stream)

    def process_batches_manager(
        self, batches: List[List[Any]]
    ) -> List[str]:
        results: List[str] = []
        for stream, batch in zip(self.streams, batches):
            result: str = stream.process_batch(batch)
            results.append(result)
        return results

    def filter_data_manager(
        self, batches: List[List[Any]], criteria: Optional[str] = None
    ) -> List[List[Any]]:
        filtered: List[List[Any]] = []
        for stream, batch in zip(self.streams, batches):
            filtered.append(stream.filter_data(batch, criteria))
        return filtered

    def get_stats_manager(self) -> List[Dict[str, Union[str, int, float]]]:
        return [stream.get_stats() for stream in self.streams]


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    s_stream: SensorStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {s_stream.stream_id}, Type: {s_stream.type}")
    result_s: str = s_stream.process_batch(
        ["temp:25", "humidity:65", "pressure:1013"]
    )
    print(result_s)

    print()
    print("Initializing Transaction Stream...")
    t_stream: TransactionStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {t_stream.stream_id}, Type: {t_stream.type}")
    result_t: str = t_stream.process_batch(
        ["buy:100", "sell:150", "buy:75"]
    )
    print(result_t)

    print()
    print("Initializing Event Stream...")
    e_stream: EventStream = EventStream("EVENT_001")
    print(f"Stream ID: {e_stream.stream_id}, Type: {e_stream.type}")
    result_e: str = e_stream.process_batch(["login", "error", "logout"])
    print(result_e)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    s_processor: StreamProcessor = StreamProcessor()
    s_processor.add_stream_manager(SensorStream("SENSOR_001"))
    s_processor.add_stream_manager(TransactionStream("TRANS_001"))
    s_processor.add_stream_manager(EventStream("EVENT_001"))

    batches: List[List[Any]] = [
        ["temp:20", "pressure:1013"],
        ["buy:200", "sell:50", "buy:30", "sell:120"],
        ["login", "error", "logout"],
    ]

    results: List[str] = s_processor.process_batches_manager(batches)
    print("\nBatch 1 Results:")
    for result in results:
        print(f"- {result}")

    print()
    print("Stream filtering active: High-priority data only")
    sensor_filtered: List[Any] = s_processor.streams[0].filter_data(
        ["temp:0", "humidity:30", "temp:50"], "temp"
    )
    trans_filtered: List[Any] = s_processor.streams[1].filter_data(
        ["buy:200", "sell:50", "buy:30", "sell:10"]
    )
    print(
        f"Filtered results: {len(sensor_filtered)} critical sensor alerts, "
        f"{len(trans_filtered)} large transaction"
    )
    print()
    print("All streams processed successfully. Nexus throughput optimal.")

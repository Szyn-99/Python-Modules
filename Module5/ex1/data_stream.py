from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for all data streams in the Nexus."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.type: str = "Generic Stream"
        self.processed_count: int = 0
        self.error_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data. Must be overridden by subclasses."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str]
    ) -> List[Any]:
        """Filter data based on criteria. Can be overridden."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics. Can be overridden."""
        return {
            "stream_id": self.stream_id,
            "type": self.type,
            "processed": self.processed_count,
            "errors": self.error_count,
        }


class SensorStream(DataStream):
    """Stream for processing environmental sensor data."""

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

            if data_batch:
                for item in data_batch:
                    if not isinstance(item, str) or ":" not in item:
                        self.error_count += 1
                        continue
                    key, value = item.split(":", 1)
                    self.processed_count += 1
                    if key == "temp":
                        self.total_temp += float(value)
                        self.temp_count += 1

            avg_temp: float = (
                self.total_temp / self.temp_count
                if self.temp_count > 0
                else 0.0
            )
            result: str = (
                f"Sensor analysis: {self.processed_count} readings processed, avg temp: {avg_temp}°C"
            )
            result: str = result + f"{self.error_count} error detected" if self.error_count > 0 else result
            return result
        except Exception as e:
            return f"Sensor processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter sensor data, defaults to critical alerts."""
        if criteria is None:
            criteria = "temp"
        filtered: List[Any] = []
        for item in data_batch:
            if isinstance(item, str) and criteria in item:
                filtered.append(item)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor-specific statistics."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["avg_temp"] = (
            self.total_temp / self.temp_count
            if self.temp_count > 0
            else 0.0
        )
        return stats


class TransactionStream(DataStream):
    """Stream for processing financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"
        self.net_flow: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transactions like 'buy:100', 'sell:150'."""
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
                        self.net_flow -= amount
                    elif action == "sell":
                        self.net_flow += amount

            sign: str = "+" if self.net_flow >= 0 else ""
            result = (
                    f"Transaction analysis: {self.processed_count} operations, "
                    f"net flow: {sign}{self.net_flow:.0f} units, "
            )
            return (
                result +  f"{self.error_count} error detected" if self.error_count > 0 else result
            )
        except Exception as e:
            return f"Transaction processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter transactions, defaults to large transactions."""
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
        """Return transaction-specific statistics."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["net_flow"] = self.net_flow
        return stats


class EventStream(DataStream):
    """Stream for processing system event data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"
        self.error_events: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process events like 'login', 'error', 'logout'."""
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
            return result +  f"{self.error_count} error detected" if self.error_count > 0 else result
        except Exception as e:
            return f"Event processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter events, defaults to error events."""
        if criteria is None:
            criteria = "error"
        return [
            item for item in data_batch
            if isinstance(item, str) and criteria in item
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event-specific statistics."""
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["error_events"] = self.error_events
        return stats


class StreamProcessor:
    """Manages multiple data streams polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: Union[SensorStream, TransactionStream, EventStream]) -> None:
        """Add a stream to the processor."""
        self.streams.append(stream)

    def process_all(
        self, batches: List[List[Any]]
    ) -> List[str]:
        """Process batches through all streams polymorphically."""
        results: List[str] = []
        for stream, batch in zip(self.streams, batches):
            result: str = stream.process_batch(batch)
            results.append(result)
        return results

    def filter_all(
        self, batches: List[List[Any]], criteria: Optional[str] = None
    ) -> List[List[Any]]:
        """Filter data across all streams."""
        filtered: List[List[Any]] = []
        for stream, batch in zip(self.streams, batches):
            filtered.append(stream.filter_data(batch, criteria))
        return filtered

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        """Collect stats from all streams."""
        return [stream.get_stats() for stream in self.streams]


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    # Initialize individual streams
    print("Initializing Sensor Stream...")
    sensor: SensorStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.type}")
    result_s: str = sensor.process_batch(
        ["temp:22.5", "humidity:65", "pressure:1013"]
    )
    print(result_s)

    print()
    print("Initializing Transaction Stream...")
    transaction: TransactionStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: {transaction.type}")
    result_t: str = transaction.process_batch(
        ["buy:100", "sell:150", "buy:75"]
    )
    print(result_t)

    print()
    print("Initializing Event Stream...")
    event: EventStream = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.type}")
    result_e: str = event.process_batch(["login", "error", "logout"])
    print(result_e)

    print()
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_002"))
    processor.add_stream(TransactionStream("TRANS_002"))
    processor.add_stream(EventStream("EVENT_002"))

    batches: List[List[Any]] = [
        ["temp:20", "humidity:70"],
        ["buy:200", "sell:50", "buy:30", "sell:120"],
        ["login", "error", "logout"],
    ]

    results: List[str] = processor.process_all(batches)
    print("Batch 1 Results:")
    print(f"- Sensor data: {batches[0].__len__()} readings processed")
    print(f"- Transaction data: {batches[1].__len__()} operations processed")
    print(f"- Event data: {batches[2].__len__()} events processed")

    print()
    print("Stream filtering active: High-priority data only")
    sensor_filtered: List[Any] = processor.streams[0].filter_data(
        ["temp:45", "humidity:30", "temp:50"], "temp"
    )
    trans_filtered: List[Any] = processor.streams[1].filter_data(
        ["buy:200", "sell:50", "buy:30", "sell:120"]
    )
    print(
        f"Filtered results: {len(sensor_filtered)} critical sensor alerts, "
        f"{len(trans_filtered)} large transaction"
    )

    print()
    print("All streams processed successfully. Nexus throughput optimal.")
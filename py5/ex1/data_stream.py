from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
        }


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not data_batch:
                raise ValueError("Empty sensor batch")
            numeric = [
                x for x in data_batch if isinstance(x, (int, float))
            ]
            if not numeric:
                raise ValueError("No numeric values in sensor batch")
            avg: float = sum(numeric) / len(numeric)
            self.processed_count += len(numeric)
            return (
                f"Sensor analysis: {len(numeric)} readings processed, "
                f"avg temp: {avg:.1f}°C"
            )
        except (ValueError, TypeError) as e:
            return f"SensorStream error: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [
                x for x in data_batch
                if isinstance(x, (int, float)) and x > 40
            ]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not data_batch:
                raise ValueError("Empty transaction batch")
            buys: List[Any] = [
                x for x in data_batch
                if isinstance(x, dict) and x.get("type") == "buy"
            ]
            sells: List[Any] = [
                x for x in data_batch
                if isinstance(x, dict) and x.get("type") == "sell"
            ]
            net: Union[int, float] = (
                sum(x["amount"] for x in buys)
                - sum(x["amount"] for x in sells)
            )
            self.processed_count += len(data_batch)
            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {net:+} units"
            )
        except (ValueError, TypeError, KeyError) as e:
            return f"TransactionStream error: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            return [
                x for x in data_batch
                if isinstance(x, dict) and x.get("amount", 0) > 100
            ]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not data_batch:
                raise ValueError("Empty event batch")
            errors: List[Any] = [
                x for x in data_batch
                if isinstance(x, str) and "error" in x.lower()
            ]
            self.processed_count += len(data_batch)
            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{len(errors)} error detected"
            )
        except (ValueError, TypeError) as e:
            return f"EventStream error: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "errors":
            return [
                x for x in data_batch
                if isinstance(x, str) and "error" in x.lower()
            ]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        return stats


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        if len(self.streams) != len(batches):
            raise ValueError(
                f"Stream/batch count mismatch: "
                f"{len(self.streams)} streams, {len(batches)} batches"
            )
        print("Processing mixed stream types through unified interface...\n")
        for stream, batch in zip(self.streams, batches):
            try:
                result = stream.process_batch(batch)
                stats = stream.get_stats()
                # split the message construction to keep line length <= 79
                msg = f"- {stats.get('type', stream.stream_id)}: {result}"
                print(msg)
            except Exception as e:
                print(f"- Stream {stream.stream_id} failed: {e}")

    def filter_all(
        self,
        batches: List[List[Any]],
        criterias: List[str]
    ) -> List[List[Any]]:
        return [
            stream.filter_data(batch, criteria)
            for stream, batch, criteria in zip(
                self.streams,
                batches,
                criterias
            )
        ]


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    sensor_batch: List[Any] = [22.5, 65.0, 101.3]
    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor.process_batch(sensor_batch))

    print()
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    trans_batch: List[Any] = [
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75},
    ]
    print(f"Processing transaction batch: {trans_batch}")
    print(transaction.process_batch(trans_batch))

    print()
    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    event_batch: List[Any] = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch}")
    print(event.process_batch(event_batch))

    print()
    print("=== Polymorphic Stream Processing ===")
    sp = StreamProcessor()
    sp.add_stream(SensorStream("SENSOR_002"))
    sp.add_stream(TransactionStream("TRANS_002"))
    sp.add_stream(EventStream("EVENT_002"))

    batches: List[List[Any]] = [
        [22.5, 45.1],
        [
            {"type": "buy", "amount": 100},
            {"type": "sell", "amount": 50},
            {"type": "buy", "amount": 200},
            {"type": "sell", "amount": 80},
        ],
        ["login", "error", "logout"],
    ]

    print("Batch 1 Results:")
    try:
        sp.process_all(batches)
    except ValueError as e:
        print(f"Configuration error: {e}")

    print("Stream filtering active: High-priority data only")
    criterias = ["critical", "large", "errors"]
    filtered = sp.filter_all(batches, criterias)
    print(f"Filtered sensor alerts: {len(filtered)} critical readings")

    print("\nAll streams processed successfully. Nexus throughput optimal.")

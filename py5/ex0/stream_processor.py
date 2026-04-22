from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if not isinstance(data, (list, tuple)) or len(data) == 0:
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")
            total: Union[int, float] = sum(data)
            avg: float = total / len(data)
            return (
                f"Processed {len(data)} numeric values, "
                f"sum={total}, avg={avg}"
            )
        except (ValueError, TypeError) as e:
            return f"NumericProcessor error: {e}"

    def format_output(self, result: str) -> str:
        return f"[NUMERIC] {result}"


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")
            return (
                f"Processed text: {len(data)} characters, "
                f"{len(data.split())} words"
            )
        except (ValueError, TypeError) as e:
            return f"TextProcessor error: {e}"

    def format_output(self, result: str) -> str:
        return f"[TEXT] {result}"


class LogProcessor(DataProcessor):

    LOG_LEVELS: List[str] = ["ERROR", "WARNING", "INFO"]

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or ":" not in data:
            return False
        level, message = data.split(":", 1)
        return level.strip() in self.LOG_LEVELS and message.strip() != ""

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log format")
            level, message = data.split(":", 1)
            level = level.strip()
            message = message.strip()
            if level in ("ERROR", "CRITICAL"):
                return f"[ALERT] {level} level detected: {message}"
            return f"[{level}] {level} level detected: {message}"
        except (ValueError, TypeError) as e:
            return f"LogProcessor error: {e}"

    def format_output(self, result: str) -> str:
        return f"[LOG] {result}"


def applies_data(processor: DataProcessor, data: Any) -> None:
    print(f"Initializing {type(processor).__name__}...")
    print(f"Processing data: {data}")
    is_valid = processor.validate(data)
    print("Validation: verified" if is_valid else "Validation: FAILED")
    print(processor.format_output(processor.process(data)))


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    data_samples: List[Any] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout",
    ]

    for processor, data in zip(processors, data_samples):
        applies_data(processor, data)
        print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")

    poly_data: List[Any] = [[1, 2, 3], "Hello World", "INFO: System ready"]
    i = 1
    for processor, data in zip(processors, poly_data):
        print(f"Result {i}: {processor.process(data)}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")

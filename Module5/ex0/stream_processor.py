from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        try:

            iterable = True
            error = False
            try:
                iter(data)
            except Exception:
                iterable = False

            
            if iterable:
                for i in data:
                    if (i.__class__.__name__ == "int" or
                            i.__class__.__name__ == "float") and \
                            not isinstance(i, bool):
                        continue
                    else:
                        error = True
            if not iterable:
                if (data.__class__.__name__ == "int" or
                        data.__class__.__name__ == "float") and \
                        data.__class__.__name__ != "bool":
                    iterable = False
                else:
                    error = True
            if error:
                return "[VALUE] ERROR level detected: a value is not numeric"
            return (f"Processed {len(data) if iterable else data} numeric "
                    f"values, sum={sum(data) if iterable else data}, "
                    f"avg={sum(data) / len(data) if iterable else data}")
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        iterable = True
        try:
            iter(data)
        except Exception:
            iterable = False
        if iterable:
            for i in data:
                if (i.__class__.__name__ == "int" or
                        i.__class__.__name__ == "float") and \
                        not isinstance(i, bool):
                    continue
                else:
                    print("Validation: Data is not numeric")
                    return False
        else:
            if (data.__class__.__name__ == "int" or
                    data.__class__.__name__ == "float") and \
                    data.__class__.__name__ != "bool":
                iterable = False
            else:
                print("Validation: Data is not numeric")
                return False
        print("Validation: Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        
        if data.__class__.__name__ == "str":
            return (f"Processed text: {len(data)} characters, "
                    f"{len(data.split(' '))} words")
        return ""

    def validate(self, data: Any) -> bool:
        if data is not None and data.__class__.__name__ == "str":
            print("Validation: Text data verified")
            return True
        print("Validation: Text data is not verified")
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        
        if data.__class__.__name__ == "str" and ":" in data:
            error, error_details = data.split(":")
            if "ERROR" in error:
                error_type = "ALERT"
            else:
                error_type = "INFO"
            return f'[{error_type}] {error} level detected:{error_details}'

        return "Invalid log format"

    def validate(self, data: Any) -> bool:
        if (data is not None and data.__class__.__name__ == "str" and
                ":" in data):
            print("Validation: Log entry verified")
            return True
        print("Validation: Log entry not verified")
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def log() -> None:
    
    print("Initializing Log Processor...")
    data = "ERROR: Connection timeout"
    print(f'Processing data: "{data}"')
    test = LogProcessor()
    result = test.process(data)
    test.validate(data)
    print(test.format_output(result))


def literal() -> None:
    print("Initializing Text Processor...")
    data = "Hello Nexus World"
    print(f'Processing data: "{data}"')
    test = TextProcessor()
    result = test.process(data)
    test.validate(data)
    print(test.format_output(result))


def numeric() -> None:
    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    test = NumericProcessor()
    result = test.process(data)
    test.validate(data)
    print(test.format_output(result))


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric()
    print()
    literal()
    print()
    log()
    print("\n=== Polymorphic Processing Demo ===")

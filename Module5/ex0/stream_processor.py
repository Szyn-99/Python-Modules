from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

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
    def __init__(self):
        super().__init__()
    def process(self, data: Any) -> str:
        try:
            
            iterable = True
            error = False
            try:
                iter(data)
            except Exception:
                iterable = False
            
            print("Initializing Numeric Processor...")
            print(f"Processing data: {data}")
            if iterable:
                for i in data:
                    if (i.__class__.__name__ == "int" or i.__class__.__name__ == "float") and i.__class__.__name__ != "bool":
                        continue
                    else:
                        error = True
            if not iterable:
                if (data.__class__.__name__ == "int" or data.__class__.__name__ == "float") and data.__class__.__name__ != "bool":
                    iterable = False
                else:
                    error = True
            if error:
                return f"[VALUE] ERROR level detected: a value is not numeric"
            return f"Processed {len(data) if iterable else data} numeric values, sum={sum(data) if iterable else data}, avg={sum(data) / len(data) if iterable else data:.2f}"   
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
                if (i.__class__.__name__ == "int" or i.__class__.__name__ == "float") and i.__class__.__name__ != "bool":
                    continue
                else:
                    print("Validation: Data is not numeric")
                    return False
        else:
            if (data.__class__.__name__ == "int" or data.__class__.__name__ == "float") and data.__class__.__name__ != "bool":
                iterable = False
            else:
                print("Validation: Data is not numeric")
                return False
        print("Validation: Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        print(super().format_output(result))

class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
    
    def process(self, data: Any) -> str:
        print("Initializing Text Processor...")
        print(f'Processing data: "{data}"')
        if data.__class__.__name__ == "str":
            return f"Processed text: {len(data)} characters, {len(data.split(' '))} words"
        return ""
    def validate(self, data: Any) -> bool:
        if data is not None and data.__class__.__name__ == "str":
            print("Validation: Text data verified")
            return True
        print("Validation: Text data is not verified")
        return False
    def format_output(self, result: str) -> str:
        print(super().format_output(result))

class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
    
    def process(self, data: Any) -> str:
        print("Initializing Log Processor...")
        print(f'Processing data: "{data}"')
        if data.__class__.__name__ == "str" and ":" in data:
            error, error_details = data.split(":")
            if "ERROR" in error:
                error_type = "ALERT"
            else:
                error_type = "INFO"
            return f'[{error_type}] {error} level detected: {error_details}'
    
        return "Invalid log format"
    def validate(self, data: Any) -> bool:
        if data is not None and data.__class__.__name__ == "str" and ":" in data:
            print("Validation: Log entry is verified")
            return True
        print("Validation: Log entry is not verified")
        return False
    
    def format_output(self, result: str) -> str:
        print(super().format_output(result))    


def log():
    data = "ERROR: Connection timeout"
    test = LogProcessor()
    result = test.process(data)
    test.validate(data)
    test.format_output(result)
def literal():
    data = "Szyn"
    test = TextProcessor()
    result = test.process(data)
    test.validate(data)
    test.format_output(result)
    print()
    print()
def numeric() -> None:
    data = True
    test = NumericProcessor()
    result = test.process(data)
    test.validate(data)
    test.format_output(result)
    print()
    print()
if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric()
    literal()
    log()
    print("=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")
    processors = (NumericProcessor(), TextProcessor(), LogProcessor(),)
    data = [[2, 2, 2],"Vasto Lorde","INFO: System ready"]

    for i , (proc, value) in enumerate(zip(processors, data)):
        print(f"Result {i}: {proc.process(value)}")

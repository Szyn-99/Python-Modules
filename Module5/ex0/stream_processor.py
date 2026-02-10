from abc import ABC, abstractmethod
from typing import Any
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
        pass
    
class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
    def process(self, data: Any) -> str:
        try:
            print("Initializing Numeric Processor...")
            print(f"Processing data: {data}")
            iterable = True
            valid = False
            try:
                iter(data)
            except Exception:
                iterable = False            
            if iterable:
                for i in data:
                    if i.__class__.__name__ == "int" or i.__class__.__name__ == "float":
                        valid = True
                    else:
                        valid = False
                        break
            else:                
                if data.__class__.__name__ == "int" or data.__class__.__name__ == "float":
                    iterable = 2
                    valid = True
                else:
                    valid = False
            return valid, iterable, data
        except Exception:
            return False, False, None
    
    def validate(self, data):
        iterable = True
        try:
            iter(data)
        except Exception:
            iterable = False
        if iterable:
            for i in data:
                if i.__class__.__name__ == "int" or i.__class__.__name__ == "float":
                    continue
                else:
                    print("Validation: Data is not numeric")
                    return False
        else:
            if data.__class__.__name__ == "int" or data.__class__.__name__ == "float":
                iterable = False
            else:
                print("Validation: Data is not numeric")
                return False
        print("Validation: Numeric data verified")
        return True

    def format_output(self, result):
        valid , iterable, data = result
        if valid and iterable == 2:
            print(f"Output: Processed {data} numeric values, sum={data}, avg={data}")
        elif valid and iterable:
            print(f"Output: Processed {len(data)} numeric values, sum={sum(data)}, avg={sum(data) / len(data):.2f}")
        else:
            print("Output: Invalid data, no process output")

class TextProcessor(ABC):
    def __init__(self):
        super().__init__()
    
    def process(self, data: Any) -> str:
        print(f'Processing data: "{data}"')
    def validate(self, data: Any) -> bool:
        if data is not None and data.__class__.__name__ == "str":
            print("Text data verified")
            return True
        print("Text data is NOT verified")
        return False
    def 

     
def numeric() -> None:
    data = [1, 2, 3, 4, 5]
    test = NumericProcessor()
    result = test.process(data)
    test.validate(data)
    test.format_output(result)
numeric()
            
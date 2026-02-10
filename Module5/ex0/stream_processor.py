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
    def process(self, data: Any) -> str:
        
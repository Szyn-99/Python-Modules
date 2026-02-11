from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional



class DataStream(ABC):
    def __init__(self, stream_id):
        self.stream_id = stream_id
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass

class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.type = "Environmental Data"
    def process_batch(self, data_batch: List[Any]) -> str:
        readings = 0
        print(f"Processing sensor batch: {data_batch}")
        if data_batch:
            lis = [(t.split(":")[0], t.split(":")[1]) for t in data_batch]
            for 
a = SensorStream("SENSOR")
a.process_batch(["temp:22", "humidity:11", "alo:3"])
            

class TransactionStream(DataStream):
    pass
class EventStream(DataStream):
    pass
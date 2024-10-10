from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar
from abc import ABC
from typing import Generic, TypeVar

T1 = TypeVar('T1')
T2 = TypeVar('T2')


class Mapper(ABC, Generic[T1, T2]):
    @staticmethod
    @abstractmethod
    def map(value: T1) -> T2:
        pass

    @staticmethod
    @abstractmethod
    def reverseMap(value: T2) -> T1:
        pass

    @staticmethod
    @abstractmethod
    def mapList(values: Optional[List[T1]]) -> List[T2]:
        returnValues: List[T2] = []
        if values is None:
            return returnValues
        for value in values:
            returnValues.append(Mapper.map(value))
        return returnValues

    @staticmethod
    @abstractmethod
    def reverseMapList(values: Optional[List[T2]]) -> List[T1]:
        returnValues: List[T1] = []
        if values is None:
            return returnValues
        for value in values:
            returnValues.append(Mapper.reverseMap(value))
        return returnValues

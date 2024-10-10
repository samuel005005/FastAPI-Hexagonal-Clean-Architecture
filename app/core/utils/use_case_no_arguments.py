from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Type = TypeVar('Type')


class UseCaseNoArgument(ABC, Generic[Type]):

    @abstractmethod
    async def execute(self) -> Type:
        pass

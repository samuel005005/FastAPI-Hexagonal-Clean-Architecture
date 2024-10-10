from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Type = TypeVar('Type')
Arguments = TypeVar('Arguments')


class UseCaseArgument(ABC, Generic[Type, Arguments]):

    @abstractmethod
    async def execute(self, arguments: Arguments) -> Type:
        pass

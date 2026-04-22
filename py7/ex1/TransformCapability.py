from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self, state: str) -> None:
        self.state = state

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

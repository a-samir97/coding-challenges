from abc import abstractmethod, ABC


class WCCommandStrategy(ABC):

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

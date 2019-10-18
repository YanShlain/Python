from abc import abstractmethod, ABC


class AbsStrategyBase(ABC):

    @abstractmethod
    def calculate(self, order):
        """ Calculate shipping cost """
        pass

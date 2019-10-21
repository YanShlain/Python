import abc
from pizza import Pizza

class AbsBuilder(object):
    __metaclass__ = abc.ABCMeta

    def get_pizza(self):
        return self._pizza

    def new_pizza(self):
        self._pizza = Pizza()

    @abc.abstractmethod
    def make_crust(self):
        pass

    @abc.abstractmethod
    def add_sauce(self):
        pass

    @abc.abstractmethod
    def add_meat(self):
        pass

    @abc.abstractmethod
    def add_vegies(self):
        pass

    @abc.abstractmethod
    def add_cheese(self):
        pass



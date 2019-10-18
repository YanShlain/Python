from strategy_class_based.strategy_base import AbsStrategyBase


class PostalStrategy(AbsStrategyBase):
    def calculate(self, order):
        return 5.00

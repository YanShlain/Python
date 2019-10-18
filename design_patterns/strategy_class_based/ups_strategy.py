from strategy_class_based.strategy_base import AbsStrategyBase


class UpsStrategy(AbsStrategyBase):
    def calculate(self, order):
        return 4.00

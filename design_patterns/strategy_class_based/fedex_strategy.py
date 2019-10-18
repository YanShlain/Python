from strategy_class_based.strategy_base import AbsStrategyBase


class FedExStrategy(AbsStrategyBase):
    def calculate(self, order):
        return 3.00

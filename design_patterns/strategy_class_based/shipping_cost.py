from strategy_class_based.shipper import Shipper


class ShippingCost:
    def __init__(self, strategy):
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate(order)
    #     if order.shipper == Shipper.FedEx:
    #         return self._fedex_cost(order)
    #
    #     if order.shipper == Shipper.UPS:
    #         return self._ups_cost(order)
    #
    #     if order.shipper == Shipper.Postal:
    #         return self._postal_cost(order)
    #
    #     raise ValueError(f"Invalid shipper {order.shipper}")
    #
    # def _fedex_cost(self, order):
    #     return 3.00
    #
    # def _ups_cost(self, order):
    #     return 4.00
    #
    # def _postal_cost(self, order):
    #     return 5.00

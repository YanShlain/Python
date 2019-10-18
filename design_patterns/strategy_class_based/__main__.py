from strategy_class_based.fedex_strategy import FedExStrategy
from strategy_class_based.order import Order
from strategy_class_based.postal_strategy import PostalStrategy
from strategy_class_based.shipper import Shipper
from strategy_class_based.shipping_cost import ShippingCost

# Test Federal Express shipping
from strategy_class_based.ups_strategy import UpsStrategy

order = Order(Shipper.FedEx)
concrete_strategy = FedExStrategy()
cost_calculator = ShippingCost(concrete_strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.00

# Test UPS shipping

order = Order(Shipper.FedEx)
concrete_strategy = UpsStrategy()
cost_calculator = ShippingCost(concrete_strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.00

# Test Postal shipping

order = Order(Shipper.FedEx)
concrete_strategy = PostalStrategy()
cost_calculator = ShippingCost(concrete_strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.00

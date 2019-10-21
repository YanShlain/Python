from strategy_delegate_based.order import Order
from strategy_delegate_based.shipper import Shipper
from strategy_delegate_based.shipping_cost import ShippingCost


# Test Federal Express shipping

def fedex_strategy(order):
    return 3.00


order = Order(Shipper.FedEx)
concrete_strategy = fedex_strategy
cost_calculator = ShippingCost(concrete_strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.00

# Test UPS shipping

order = Order(Shipper.FedEx)
concrete_strategy = lambda order: 4.0  # Bed practice ! Should use def
cost_calculator = ShippingCost(concrete_strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.00

# Test Postal shipping

order = Order(Shipper.FedEx)
cost_calculator = ShippingCost(lambda order: 5.00)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.00

print("Test passed")

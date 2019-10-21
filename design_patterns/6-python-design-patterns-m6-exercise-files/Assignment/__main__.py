from pizza_maker import PizzaMaker
from my_pizza import MyPizza

pizza_maker = PizzaMaker(MyPizza())
pizza_maker.make_pizza()
pizza = pizza_maker.get_pizza()
pizza.display()
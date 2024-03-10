from coffee import Coffee  # Import the Coffee class
from order import Order    # Import the Order class

class Customer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise Exception("Invalid coffee provided")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise Exception("Invalid price provided")
        order = Order(self, coffee, price)
        orders.append(order)  # Append the order to the orders list
        return order

# Define the orders list outside the class
orders = []

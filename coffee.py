from order import Order  

class Coffee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def add_order(self, price):
        # Create an Order instance and add it to the list of orders
        order = Order(None, self, price)  # The customer argument can be None for now
        orders.append(order)

    def orders(self):
        return [order for order in orders if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        coffee_orders = self.orders()
        if not coffee_orders:
            return 0
        total_price = sum(order.price for order in coffee_orders)
        return total_price / len(coffee_orders)

# Define the orders list outside the class
orders = []

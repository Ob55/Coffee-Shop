from customer import Customer
from coffee import Coffee
from order import Order

def test_order_properties():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 4.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.0

import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name():
    customer = Customer("John")
    assert customer.name == "John"

def test_customer_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_customer_create_order_invalid_input():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    with pytest.raises(Exception):
        customer.create_order(coffee, "invalid_price")

# Add more test cases as needed

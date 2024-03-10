from coffee import Coffee

def test_average_price():

    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    
  

    assert coffee1.average_price() == 0
    assert coffee2.average_price() == 0
    
    coffee1.add_order(5.0) 
    coffee1.add_order(4.0)  
    coffee2.add_order(6.0) 
    

    assert coffee1.average_price() == 4.5 
    assert coffee2.average_price() == 6.0  
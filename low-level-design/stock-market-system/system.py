from order import Order

class __StockExchange(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__StockExchange, cls).__new__(cls)
    return cls.__instances

class StockExchange(metaclass=__StockExchange):
  def __init__(self):
    pass
    
  def place_order(order: Order):
    pass
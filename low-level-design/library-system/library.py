# The Library is a singleton class that ensures it will have only one active instance at a time

from address import Address

class __Library():
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__Library, cls).__new__(cls)
    return cls.__instances

class Library(metaclass = __Library):
  def __init__(self, id: int, name: str, address: Address):
    self.__id = id
    self.__name = name
    self.__address = address

  def get_address(self):
    None
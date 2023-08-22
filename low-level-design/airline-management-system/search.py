from abc import ABC, abstractmethod

class Search(ABC):
  def search_flight(self, source, dest, arrival, departure):
    pass

class SearchCatalog(Search):
  def __init__(self):
    self.__flights = {}

  def search_flight(self, source, dest, arrival, departure):
    # functionality
    pass

from abc import ABC, abstractmethod
class Search(ABC):
    def search(style, start_date, duration):
        None


class Catalog(Search):
    def __init__(self):
        self.__rooms = []

    def search(style, date, duration):
        None
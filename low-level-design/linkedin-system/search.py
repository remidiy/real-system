from abc import ABC, abstractmethod

class Search(ABC):
  def search_user(self, name):
    pass
  def search_company(self, name):
    pass
  def search_group(self, name):
    pass
  def search_job(self, title):
    pass

class SearchCatalog(Search):
  def __init__(self):
    self.__users = {}
    self.__companies = {}
    self.__groups = {}
    self.__jobs = {}

  def add_new_user(self, user):
    pass
  def add_new_company(self, company):
    pass
  def add_new_group(self, group):
    pass
  def add_new_job(self, job):
    pass

  def search_user(self, name):
    pass
  def search_company(self, name):
    pass
  def search_group(self, name):
    pass
  def search_job(self, title):
    pass
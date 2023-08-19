from enums import AccountStatus


class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country

class Account:
  def __init__(self, id, password, status=AccountStatus.ACTIVE):
    self.__id = id
    self.__password = password
    self.__status = status

  def reset_password(self):
    None
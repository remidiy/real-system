class Admin:
  def __init__(self):
    None
  def add_player(self, player):
    None  
  def add_team(self, team):
    None
  def add_match(self, match):
    None 
  def add_tournament(self, tournament):
    None
  def add_stats(self, stats):
    None 
  def add_news(self, news):
    None

class Player:
  def __init__(self, name, age, country, position, teams, stat):
    self.__namer = name
    self.__age = age
    self.__country = country
    self.__position = position
    self.__teams = teams
    self.__stat = stat

class Coach:
  def __init__(self, name, age, country, teams):
    self.__namer = name
    self.__age = age
    self.__country = country
    self.__teams = teams

class Umpire:
  def __init__(self, name, age, country):
    self.__namer = name
    self.__age = age
    self.__country = country

  def assign_match(match):
    None
    
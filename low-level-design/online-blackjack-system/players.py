from abc import ABC, abstractmethod
from deck import Card


class Hand:
  def __init__(self, cards):
    self.__cards = []

  def get_scores(self):
    None

  def add_card(self, card):
    None

class Player:
  def __init__(self, id, password, balance, status, person, hand):
    self.__id = id
    self.__password = password
    self.__balance = balance
    self.__status = status
    self.__person = person
    self.__hand = hand

  def add_hand(self, hand: Hand):
    pass
  def remove_hand(self, hand: Hand):
    pass
  def add_card_to_hand(self, card: Card, hand: Hand):
    pass
  
  @abstractmethod
  def reset_password(self):
    pass

class BlackjackPlayer(Player):
  def __init__(self, id, password, balance, status, person, hand, bet, total_cash):
    super().__init__(id, password, balance, status, person, hand)
    self.__bet = bet
    self.__total_cash = total_cash

  def place_bet(self, bet: int):
    pass
  
  def reset_password(self):
    pass

class Dealer(Player):
  def __init__(self, id, password, balance, status, person, hand,):
    super().__init__(id, password, balance, status, person, hand)

  def get_total_score(self):
    None

  def reset_password(self):
    pass
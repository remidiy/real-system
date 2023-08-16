class Card:
  def __init__(self, suit, face_value):
    self.__suit = suit
    self.__face_value = face_value

class Deck:
  def __init__(self, cards):
    self.__cards = []

  def get_cards(self):
    None

class Shoe:
  def __init__(self, decks, number_of_decks):
    self.__decks = {}
    self.__number_of_decks = number_of_decks

  def create_shoe(self):
    None

  def shuffle(self):
    None

  def deal_card(self):
    None
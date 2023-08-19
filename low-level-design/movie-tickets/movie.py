class Movie:

  def __init__(self, title, genre, language, release_date, duration):
    self.__title = title
    self.__genre = genre
    self.__release_date = release_date
    self.__language = language
    self.__duration = duration
    self.__shows = [] # List of shows

class ShowTime:

  def __init__(self, show_id, start_time, date, duration):
    self.__show_id = show_id
    self.__start_time = start_time
    self.__date = date
    self.__duration = duration
    self.__seats = [] # List of seats

  def show_available_seats():
    pass

class MovieTicket:
  
  def __init__(self, ticket_id, seat, movie, show):
    self.__ticket_id = ticket_id
    self.__seat = seat # References an instance of the Seat class
    self.__movie = movie # References an instance of the Movie class
    self.__show = show # References an instance of the ShowTime class
class Itinerary:
  def __init__(self, starting_airport, final_airport, creation_date, reservations, passengers):
    self.__starting_airport = starting_airport
    self.__final_airport = final_airport
    self.__creation_date = creation_date
    self.__reservations = reservations
    self.__passengers = passengers

  def make_reservation(self):
    pass 

  def make_payment(self):
    pass 

class FlightReservation:
  def __init__(self, reservation_number, flight, seat_map, status, creation_date):
    self.__reservation_number = reservation_number 
    self.__flight = flight
    self.__seat_map = seat_map
    self.__status = status
    self.__creation_date = creation_date
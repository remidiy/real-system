class Seat:
  def __init__(self, seat_number, type, _class):
    self.__seat_number = seat_number 
    self.__type = type
    self.___class = _class


class FlightSeat(Seat):
  def __init__(self, fare, status, reservation_number, seat_number, type, _class):
    self.__fare = fare
    self.__status = status
    self.__reservation_number = reservation_number
  
    super().__init__(seat_number, type, _class)
  
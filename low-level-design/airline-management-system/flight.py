class Flight:
  def __init__(self, flight_no, duration_min, departure, arrival):
    self.__flight_no = flight_no 
    self.__duration_min = duration_min
    self.__departure = departure
    self.__password = arrival
    self.__instances = []


class FlightInstance:
  def __init__(self, flight, departureTime, gate, status, aircraft, seats):
    self.__flight = flight 
    self.__departureTime = departureTime
    self.__gate = gate
    self.__status = status
    self.__aircraft = aircraft
    self.__seats = seats
  
from abc import ABC, abstractmethod

class Stat(ABC):
  def __init__(self):
    None

  @abstractmethod
  def update_stats(self):
    None

class PlayerStat(Stat):
  def __init__(self, ranking, best_score, best_wicket_count, total_matches_played, total100s, total_hattricks):
    self.__ranking = ranking
    self.__best_score = best_score
    self.__best_wicket_count = best_wicket_count
    self.__total_matches_played = total_matches_played
    self.__total100s = total100s
    self.__total_hattricks = total_hattricks

  def update_stats(self):
    None

class MatchStat(Stat):
  def __init__(self, win_percentage, top_batsman, top_bowler):
    self.__win_percentage = win_percentage
    self.__top_batsman = top_batsman
    self.__top_bowler = top_bowler
  
  def update_stats(self):
    None

class TeamStat(Stat):
  def __init__(self, total_sixes, total_fours, total_reviews):
    self.__total_sixes = total_sixes
    self.__total_fours = total_fours
    self.__total_reviews = total_reviews
  
  def update_stats(self):
    None
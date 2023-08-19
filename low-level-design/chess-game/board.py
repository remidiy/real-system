class Box:
  def __init__(self, piece, x, y):
    self.__piece = piece
    self.__x = x
    self.__y = y

class Chessboard:
  def __init__(self, boxes, creation_date):
    self.__boxes = boxes
    self.__creation_date = creation_date

  def get_pieces(self):
    pass
  def reset_board(self):
    pass
  def update_board(self):
    pass

from abc import ABC, abstractmethod
class Piece(ABC):
  def __init__(self, killed, white):
    self.__killed = killed
    self.__white = white

  def is_white(self):
    pass
    
  def is_killed(self):
    pass

  @abstractmethod
  def can_move(self, board, start, end):
    pass

class King(Piece):
  def __init__(self, killed, white, castling_done):
    super().__init__(killed, white)
    self.__castling_done = False
  
  def can_move(self, board, start, end):
    pass

class Queen(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass

class Knight(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass

class Bishop(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass

class Rook(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass

class Pawn(Piece):
  def __init__(self, killed, white):
    super().__init__(killed, white)
  
  def can_move(self, board, start, end):
    pass
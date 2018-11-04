class Piece:
  def __init__(self, color):
    self.color = color

  def get_char(self):
    return chr(self.code if color == "white" else self.code + 6)

  def get_name(self):
    return "{}-{}".format(self.color, self.__class__.__name__.lower())

class Pawn(Piece):
  code = 9817

class Knight(Piece):
  code = 9816

class Rook(Piece):
  code = 9814

class Bishop(Piece):
  code = 9815

class King(Piece):
  code = 9812

class Queen(Piece):
  code = 9813

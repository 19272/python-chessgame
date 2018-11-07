class Piece:
  def __init__(self, color, position):
    self.color = color
    self.position = position

  def get_char(self):
    return chr(self.code if color == "white" else self.code + 6)

  def get_name(self):
    return "{}-{}".format(self.color, self.__class__.__name__.lower())

  def is_legal(self, target):
    return True

  def destroy(self):
    self.position = None

class Pawn(Piece):
  code = 9817

  def find_legal_moves(self, board):

    posX, posY = self.position
    color_coefficient = 1 if self.color == "white" else -1
    first_line = 1 if self.color == "white" else 6
    moves = []

    # VERTICAL MOVE + 1
    if (posX, posY + color_coefficient) in board \
    and not board[(posX, posY + color_coefficient)]:
      moves.append((posX, posY + color_coefficient))

    # VERTICAL MOVE + 2
    if posY == first_line \
    and not board[(posX, posY + 2 * color_coefficient)]:
      moves.append((posX, posY + 2 * color_coefficient))

    # DIAGONAL MOVE
    for x in [-1, 1]:
      if (posX + x, posY + color_coefficient) in board \
      and board[(posX + x, posY + color_coefficient)] \
      and board[(posX + x, posY + color_coefficient)].color != self.color:
        moves.append((posX + x, posY + color_coefficient))

    return moves

class Knight(Piece):
  code = 9816

  def find_legal_moves(self, board):

    posX, posY = self.position
    moves = []

    for x in [-2, -1, 1, 2]:
      for y in [(3 - abs(x)), -(3 - abs(x))]:

        if (posX + x, posY + y) in board:
          if not board[(posX + x, posY + y)] \
          or board[(posX + x, posY + y)].color != self.color:
            moves.append((posX + x, posY + y))

    return moves

class Rook(Piece):
  code = 9814

  def find_legal_moves(self, board):

    posX, posY = self.position
    moves = []

    for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

      distance = 1
      while (posX + distance * x, posY + distance * y) in board:
        if not board[(posX + distance * x, posY + distance * y)]:
          moves.append((posX + distance * x, posY + distance * y))
        elif board[(posX + distance * x, posY + distance * y)].color != self.color: #
          moves.append((posX + distance * x, posY + distance * y))
          break
        else:
          break
        distance += 1

    return moves


class Bishop(Piece):
  code = 9815

  def find_legal_moves(self, board):

    posX, posY = self.position
    moves = []

    for x in [-1, 1]:
      for y in [-1, 1]:
        distance = 1

        while (posX + distance * x, posY + distance * y) in board:
          if not board[(posX + distance * x, posY + distance * y)]:
            moves.append((posX + distance * x, posY + distance * y))
          elif board[(posX + distance * x, posY + distance * y)].color != self.color:
            moves.append((posX + distance * x, posY + distance * y))
            break
          else:
            break
          distance += 1

    return moves

class King(Piece):
  code = 9812

class Queen(Piece):
  code = 9813

  def find_legal_moves(self, board):
    posX, posY = self.position
    moves = []

    # SAME AS IN ROOK
    for x in [-1, 1, 0]:
      y_var = [0] if x != 0 else [-1, 1]
      for y in y_var:

        distance = 1
        while (posX + distance * x, posY + distance * y) in board:
          if not board[(posX + distance * x, posY + distance * y)]:
            moves.append((posX + distance * x, posY + distance * y))
          elif board[(posX + distance * x, posY + distance * y)].color != self.color:
            moves.append((posX + distance * x, posY + distance * y))
            break
          else:
            break
          distance += 1

    # SAME AS IN BISHOP
    for x in [-1, 1]:
      for y in [-1, 1]:
        distance = 1

        while (posX + distance * x, posY + distance * y) in board:
          if not board[(posX + distance * x, posY + distance * y)]:
            moves.append((posX + distance * x, posY + distance * y))
          elif board[(posX + distance * x, posY + distance * y)].color != self.color:
            moves.append((posX + distance * x, posY + distance * y))
            break
          else:
            break
          distance += 1

    return moves

from pieces import *

class ChessBoard:

  def __init__(self):
    self.selected = None
    self.legal_moves = []
    self.turn = "white"

    self.board = {}

    for row in range(8):
      for column in range(8):
        self.board[(row, column)] = None

    for column in range(8):
      self.board[(column, 1)] = Pawn("white", (column, 1))
      self.board[(column, 6)] = Pawn("black", (column, 6))

    self.board[(0, 0)] = Rook("white", (0, 0))
    self.board[(7, 0)] = Rook("white", (7, 0))
    self.board[(0, 7)] = Rook("black", (0, 7))
    self.board[(7, 7)] = Rook("black", (7, 7))

    self.board[(1, 0)] = Knight("white", (1, 0))
    self.board[(6, 0)] = Knight("white", (6, 0))
    self.board[(1, 7)] = Knight("black", (1, 7))
    self.board[(6, 7)] = Knight("black", (6, 7))

    self.board[(2, 0)] = Bishop("white", (2, 0))
    self.board[(5, 0)] = Bishop("white", (5, 0))
    self.board[(2, 7)] = Bishop("black", (2, 7))
    self.board[(5, 7)] = Bishop("black", (5, 7))

    self.board[(4, 0)] = Queen("white", (4, 0))
    self.board[(4, 7)] = Queen("black", (4, 7))

    self.board[(3, 0)] = King("white", (3, 0))
    self.board[(3, 7)] = King("black", (3, 7))

  def click_handler(self, value):
    if not self.selected:
      return self.__set_selected(value)
    else:
      return self.__move_piece(value)

  def __set_selected(self, value):

    if self.board[value] is not None \
    and self.board[value].color == self.turn:

      # SET SELECTED CELL
      self.selected = value

      # SET POSSIBLE MOVES
      self.legal_moves = self.board[value].find_legal_moves(self.board)

      print("Selected : {}".format(self.selected))
      print("Legal moves :")
      for i in self.legal_moves:
        print(i)
      print("-----------------")

      return True

    else:
      return False

  def __change_turn(self):
    self.turn = "white" if self.turn == "black" else "black"

  def __move_piece(self, target):

    if target in self.legal_moves:

      # UPDATING PIECE'S ATTRIBUTES
      self.board[self.selected].position = target
      if self.board[target]:
        self.board[target].destroy()

      # UPDATING BOARD
      self.board[target] = self.board[self.selected]
      self.board[self.selected] = None

      # SET NEXT TURN
      self.selected = None
      self.legal_moves = []
      self.__change_turn()

      return True

    else:

      # UNSELECT PIECE
      self.selected = None
      self.legal_moves = []
      return False


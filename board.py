from pieces import *

class ChessBoard:

  def __init__(self):
    self.board = {}

    self.board["A8"] = Rook("black")
    self.board["H8"] = Rook("black")
    self.board["A1"] = Rook("white")
    self.board["H1"] = Rook("white")

    self.board["B8"] = Knight("black")
    self.board["G8"] = Knight("black")
    self.board["B1"] = Knight("white")
    self.board["G1"] = Knight("white")

    self.board["C8"] = Bishop("black")
    self.board["F8"] = Bishop("black")
    self.board["C1"] = Bishop("white")
    self.board["F1"] = Bishop("white")

    self.board["D8"] = Queen("black")
    self.board["D1"] = Queen("white")

    self.board["E8"] = King("black")
    self.board["E1"] = King("white")

    for column in range(ord("A"), ord("H") + 1):
      self.board[chr(column) + "7"] = Pawn("black")

    for column in range(ord("A"), ord("H") + 1):
      self.board[chr(column) + "2"] = Pawn("white")

    for row in range(3, 7):
      for column in range(ord("A"), ord("H") + 1):
        self.board[chr(column) + str(row)] = None


  def print_board(self):

    print("\n ", end="  ")
    for columnn in range(ord("A"), ord("H") + 1):
      print(chr(columnn), end=" ")
    print("\n")

    for row in range(1, 9):
      print(row, end="  ")
      for columnn in range(ord("A"), ord("H") + 1):
        if self.board[chr(columnn) + str(row)]:
          print(self.board[chr(columnn) + str(row)].symbol, end=" ")
        else:
          print(" ", end=" ")
      print("  " + str(row))

    print("\n ", end="  ")
    for columnn in range(ord("A"), ord("H") + 1):
      print(chr(columnn), end=" ")
    print("\n")

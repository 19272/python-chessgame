from board import ChessBoard
from pieces import *

def NewGame():
  board = ChessBoard()
  board.resume()

a = NewGame()

  # def print_board(self):

  #   print("\n ", end="  ")
  #   for columnn in range(ord("A"), ord("H") + 1):
  #     print(chr(columnn), end=" ")
  #   print("\n")

  #   for row in range(1, 9):
  #     print(row, end="  ")
  #     for columnn in range(ord("A"), ord("H") + 1):
  #       if self.board[chr(columnn) + str(row)]:
  #         print(self.board[chr(columnn) + str(row)].symbol, end=" ")
  #       else:
  #         print(" ", end=" ")
  #     print("  " + str(row))

  #   print("\n ", end="  ")
  #   for columnn in range(ord("A"), ord("H") + 1):
  #     print(chr(columnn), end=" ")
  #   print("\n")

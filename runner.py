# run java -jar processing-py.jar test.py
from pieces import *

board = {}

for row in range(8):
  for column in range(8):
    board[(row, column)] = None

for column in range(8):
  board[(column, 1)] = Pawn("white")
  board[(column, 6)] = Pawn("black")

board[(0, 0)] = Rook("white")
board[(7, 0)] = Rook("white")
board[(0, 7)] = Rook("black")
board[(7, 7)] = Rook("black")

board_size = 560
cell_width = board_size / 8

def setup():
  size(board_size, board_size)

def draw():
  for x, y in board:
    posX = x * cell_width
    posY = y * cell_width
    if ((x + (y % 2)) % 2) == 0:
      fill(237, 218, 185)
    else:
      fill(175, 136, 104)
    rect(posX, posY, cell_width, cell_width)
    if board[(x, y)]:
      photo = loadImage('pieces/{}.png'.format(board[(x, y)].get_name()))
      image(photo, posX + 5, posY + 5)

def mousePressed():
  print(mouseX / cell_width, mouseY / cell_width)

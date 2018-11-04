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

board[(1, 0)] = Knight("white")
board[(6, 0)] = Knight("white")
board[(1, 7)] = Knight("black")
board[(6, 7)] = Knight("black")

board[(2, 0)] = Bishop("white")
board[(5, 0)] = Bishop("white")
board[(2, 7)] = Bishop("black")
board[(5, 7)] = Bishop("black")

board[(4, 0)] = Queen("white")
board[(4, 7)] = Queen("black")

board[(3, 0)] = King("white")
board[(3, 7)] = King("black")

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
      noStroke()
    rect(posX, posY, cell_width, cell_width)
    if board[(x, y)]:
      photo = loadImage('pieces/{}.png'.format(board[(x, y)].get_name()))
      image(photo, posX + 5, posY + 5)

def mousePressed():
  print(mouseX / cell_width, mouseY / cell_width)

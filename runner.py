# java -jar processing-py.jar runner.py

from pieces import *
from board import *

# BOARD SETUP

board_size = 560
cell_width = board_size / 8

# NEW GAME SETUP

myBoard = ChessBoard()

# PROCESSING

def setup():
  size(board_size, board_size)

def draw():
  for x, y in myBoard.board:
    posX = x * cell_width
    posY = y * cell_width
    if (x, y) == myBoard.selected:
      fill(107, 110, 71)
    elif ((x + (y % 2)) % 2) == 0:
      fill(237, 218, 185)
    else:
      fill(175, 136, 104)
    noStroke()
    rect(posX, posY, cell_width, cell_width)
    if (x, y) in myBoard.legal_moves:
      if myBoard.board[(x, y)]:
        square_image = loadImage('pieces/square.png')
        image(square_image, posX, posY)
      else:
        dot_image = loadImage('pieces/dot.png')
        image(dot_image, posX + 20, posY + 20)
    if myBoard.board[(x, y)]:
      photo = loadImage('pieces/{}.png'.format(myBoard.board[(x, y)].get_name()))
      image(photo, posX + 5, posY + 5)

def mousePressed():
  clicked_cell = (mouseX / cell_width, mouseY / cell_width)
  myBoard.click_handler(clicked_cell)






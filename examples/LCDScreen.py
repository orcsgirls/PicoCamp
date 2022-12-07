import board
import busio
from rgb1602 import Screen

i2c = busio.I2C(board.GP17, board.GP16)

screen = Screen(i2c)
screen.update("Pico Camp","Love it :)")

import board
import digitalio
import time
import neopixel
from rainbowio import colorwheel


num_pixels = 8   # Number of NeoPixels on the strip

pixels = neopixel.NeoPixel(board.GP1, num_pixels, auto_write=True) # 'In' needs to connect to GP1
pixels.brightness = 0.5

while True:
    pixels.fill((255, 0, 0))


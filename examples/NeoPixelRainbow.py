import board
import digitalio
import time
import neopixel
from rainbowio import colorwheel

num_pixels = 8   # Number of NeoPixels on the strip

pixels = neopixel.NeoPixel(board.GP1, num_pixels, auto_write=False) # 'In' needs to connect to GP1
pixels.brightness = 0.5

while True:
    # Loop over all colors
    for j in range(255):
        # Loop over all pixels
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(pixel_index & 255)
        pixels.show()

    time.sleep(0.01)

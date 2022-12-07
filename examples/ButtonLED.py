import board
import digitalio
import time

# LED to GP15, button to GP13

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    led.value = button.value


import board
import busio
import digitalio
import time
import adafruit_ahtx0
from rgb1602 import Screen

# Button
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

# i2c Devices
i2c = busio.I2C(board.GP17, board.GP16)
sensor = adafruit_ahtx0.AHTx0(i2c)
screen = Screen(i2c)

while True:
    t = sensor.temperature;
    h = sensor.relative_humidity;
    
    # Check on desired units
    if(button.value):
        output = f"Temp.: {t:.1f} C"
    else:
        t = t * 9.0/5.0 + 32.0
        output = f"Temp.: {t:.1f} F"
        
    screen.update(output,f"Hum. : {h:.1f} %")
    print((t,h)) # This allows creating a chart
    
    time.sleep(1)
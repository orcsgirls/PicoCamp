import board
import busio
import time
import adafruit_ahtx0

i2c = busio.I2C(board.GP17, board.GP16)
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    print(f"\nTemperature: {sensor.temperature:.1f} C")
    print(f"Humidity: {sensor.relative_humidity:.1f} %")
    time.sleep(1)

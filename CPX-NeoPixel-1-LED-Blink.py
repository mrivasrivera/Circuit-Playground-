# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time
import neopixel

led= neopixel.NeoPixel(board.NEOPIXEL,10, auto_write=True)
led.brightness = 0.5
print(dir(led))
while True:
    led[0] = (225,0,0)
    led[1] = (25,50,0)
    led[2] = (0,0,70)
    led[3] = (100,100,0)
    led[4] = (50,75,90)
    led[9] = (225,0,0)
    led[8] = (25,50,0)
    led[7] = (0,0,70)
    led[6] = (100,100,0)
    led[5] = (50,75,90)

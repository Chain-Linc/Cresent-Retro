print("FILE: Starting ThumbyBattle.py")
print("LOADED: ThumbyBattle.py Started")
import time
print("LOADED: Time Imported")
import framebuf
print("LOADED: Framebuf Imported")
import thumby
print("LOADED: Thumby Imported")

import sys
print("LOADED: Sys Imported")
sys.path.insert(0, '/Games/ThumbyBattle')
from thumbyGrayscale import display, buttonA
print("LOADED: Thumby Grayscale Imported")
display.enableGrayscale()
print("LOADED_COMPLETE")
print("FILE: Grayscale imported and enabled")

import engine
from sprites import *

screen = engine.Screen()
screen.blit(tank)


def updateDisplay():
    screen.update()

display.setFPS(60)

thumby.audio.playBlocking(1000, 100)
thumby.audio.playBlocking(1500, 100)
thumby.audio.playBlocking(2000, 100)
while True:
    t0 = time.ticks_ms()   # Get time (ms)

    updateDisplay()
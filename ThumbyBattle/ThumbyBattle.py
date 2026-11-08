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




SCREEN_SIZE = (72, 40)

screenGSL1Buffer = framebuf.FrameBuffer(display.buffer, *SCREEN_SIZE, framebuf.MONO_VLSB)
screenGSL2Buffer = framebuf.FrameBuffer(display.shading, *SCREEN_SIZE, framebuf.MONO_VLSB)
screenGSL1PalleteBuffer = framebuf.FrameBuffer(bytearray(1), 4, 1, framebuf.MONO_VLSB)
screenGSL2PalleteBuffer = framebuf.FrameBuffer(bytearray(1), 4, 1, framebuf.MONO_VLSB)
# | Layer 1 | Layer 2 | Colour
# | 0       | 0       | Black
# | 0       | 1       | Dark gray
# | 1       | 1       | Light gray
# | 1       | 0       | White
screenGSL1PalleteBuffer.pixel(2, 0, 1)
screenGSL1PalleteBuffer.pixel(3, 0, 1)
screenGSL2PalleteBuffer.pixel(1, 0, 1)
screenGSL2PalleteBuffer.pixel(2, 0, 1)

screenBuffer = bytearray(72 * 40 // 4)
screen = framebuf.FrameBuffer(screenBuffer, *SCREEN_SIZE, framebuf.GS2_HMSB)

screen.fill_rect(0, 0, 20, 22, 3)

screen.fill_rect(0, 0, 8, 20, 0)
screen.fill_rect(10, 0, 8, 20, 1)
screen.fill_rect(20, 0, 8, 20, 2)
screen.fill_rect(30, 0, 8, 20, 3)

battleFieldBuffer = bytearray(72 * 40 // 8)
battleFieldFrame = framebuf.FrameBuffer(battleFieldBuffer, 72, 40, framebuf.MONO_VLSB)
battleFieldFrame.fill_rect(0, 20, 72, 20, 1)
battleFieldFrame.fill_rect(0, 0, 72, 20, 0)

def updateDisplay():
    screenGSL1Buffer.blit(screen, 0, 0, -1, screenGSL1PalleteBuffer)
    screenGSL2Buffer.blit(screen, 0, 0, -1, screenGSL2PalleteBuffer)
    display.update()

display.setFPS(60)

thumby.audio.playBlocking(1000, 100)
thumby.audio.playBlocking(1500, 100)
thumby.audio.playBlocking(2000, 100)
while True:
    t0 = time.ticks_ms()   # Get time (ms)

    updateDisplay()
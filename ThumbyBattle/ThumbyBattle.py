import time

import framebuf
from sys import path
path += "/Games/ThumbyBattle/"
from Games.ThumbyBattle.thumbyGrayscale import display, Sprite, buttonA
display.enableGrayscale()

SCREEN_SIZE = (72, 40)

screenGSBuffer = framebuf.FrameBuffer(display.buffer, *SCREEN_SIZE, framebuf.MONO_VLSB)
screenGSShading = framebuf.FrameBuffer(display.shading, *SCREEN_SIZE, framebuf.MONO_VLSB)

screenGSBufferPallete = bytearray([0x00])
screenGSShadingPallete = bytearray([0x00])
screenGSShadingPalleteFrame = framebuf.FrameBuffer(screenGSShadingPallete, 1, 1, framebuf.MONO_VLSB)
screenGSShadingPalleteFrame.set_pixel(0, 0, 1, 1, 0)
screenGSShadingPalleteFrame.set_pixel(1, 0, 1, 1, 1)
screenGSShadingPalleteFrame.set_pixel(2, 0, 1, 1, 2)
screenGSShadingPalleteFrame.set_pixel(3, 0, 1, 1, 3)

screenGSShadingBufferFrame = framebuf.FrameBuffer(screenGSShadingPallete, 1, 1, framebuf.MONO_VLSB)
screenGSShadingBufferFrame.set_pixel(0, 0, 1, 1, 0)
screenGSShadingBufferFrame.set_pixel(1, 0, 1, 1, 1)
screenGSShadingBufferFrame.set_pixel(2, 0, 1, 1, 2)
screenGSShadingBufferFrame.set_pixel(3, 0, 1, 1, 3)

screenBuffer = bytearray(72 * 40 // 4)
screen = framebuf.FrameBuffer(screenBuffer, *SCREEN_SIZE, framebuf.GS2_HMSB)

screen.pixel(0, 0, 0)
screen.pixel(1, 0, 1)
screen.pixel(2, 0, 2)
screen.pixel(3, 0, 3)

screen.fill_rect(0, 0, 10, 20, 0)
screen.fill_rect(10, 0, 10, 20, 1)
screen.fill_rect(20, 0, 10, 20, 2)
screen.fill_rect(30, 0, 10, 20, 3)

print(screenBuffer)

battleFieldBuffer = bytearray(72 * 40 // 8)
battleFieldFrame = framebuf.FrameBuffer(battleFieldBuffer, 72, 40, framebuf.MONO_VLSB)
battleFieldFrame.fill_rect(0, 20, 72, 20, 1)
battleFieldFrame.fill_rect(0, 0, 72, 20, 0)

def updateDisplay():
    screenGSBuffer.blit(screen, 0, 0, -1, screenGSBufferPallete)
    screenGSShading.blit(screen, 0, 0, -1, screenGSShadingPallete)
    display.update()

display.setFPS(60)

while True:
    t0 = time.ticks_ms()   # Get time (ms)

    updateDisplay()
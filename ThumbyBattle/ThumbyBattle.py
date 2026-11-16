print("FILE: Starting ThumbyBattle.py")
print("LOADED: ThumbyBattle.py Started")
import time
print("LOADED: Time Imported")
import thumby
import sys
print("LOADED: Sys Imported")
sys.path.insert(0, '/Games/ThumbyBattle')
import engine
from sprites import *

#buffer = bytearray((72 * 40) // 4)
#surface = framebuf.FrameBuffer(buffer, 72, 40, framebuf.GS2_HMSB)

#surface.fill(2)
#print(buffer)

testRect = engine.Rect(10, 10, 20, 20)
print(testRect.x, testRect.y, testRect.w, testRect.h, testRect.size)


screen = engine.Screen()
screen.surface.fill(1)
screen.surface.fill_rect(9, 9, 12, 12, 3)
screen.blit(tank_1, 10, 10)
#screen.surface.rect(10, 10, 100, 100, 2)



thumby.audio.playBlocking(1000, 100)
thumby.audio.playBlocking(1500, 100)
thumby.audio.playBlocking(2000, 100)
while True:
    t0 = time.ticks_ms()   # Get time (ms)

    screen.update()
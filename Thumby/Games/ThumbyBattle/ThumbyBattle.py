import framebuf
from sys import path
path += "/Games/ThumbyBattle/"
from thumbyGrayscale import display, Sprite, buttonA
display.enableGrayscale()

SCREEN_SIZE = (72, 40)

battleField = framebuf.FrameBuffer(bytearray(72 * 40 // 8), 72, 40, framebuf.MONO_VLSB)
battleField.fill_rect(0, 20, 72, 20, 0)
battleField.fill_rect(0, 0, 72, 20, 1)

# BITMAP: width: 32, height: 32
bitmap0 = bytearray([0,0,0,0,0,0,0,0,248,8,232,40,40,40,40,40,40,40,40,40,40,232,8,248,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,255,0,63,32,32,32,32,32,32,32,32,32,32,63,0,255,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,255,0,12,12,63,63,12,12,0,0,24,24,3,3,0,255,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,31,16,16,16,16,20,18,16,20,18,16,16,16,16,16,31,0,0,0,0,0,0,0,0])


# Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
thumbySprite = Sprite(32, 32, bitmap0)

display.setFPS(60)


while(1):
    t0 = time.ticks_ms()   # Get time (ms)
    display.fill(0) # Fill canvas to black


    bobRate = 250 # Set arbitrary bob rate (higher is slower)
    bobRange = 5  # How many pixels to move the sprite up/down (-5px ~ 5px)

    # Calculate number of pixels to offset sprite for bob animation
    bobOffset = math.sin(t0 / bobRate) * bobRange

    # Center the sprite using screen and bitmap dimensions and apply bob offset
    thumbySprite.x = int((display.width/2) - (32/2))
    thumbySprite.y = int(round((display.height/2) - (32/2) + bobOffset))

    # Display the bitmap using bitmap data, position, and bitmap dimensions
    display.drawSprite(thumbySprite)
    display.buffer = memoryview(battleField)
    display.update()


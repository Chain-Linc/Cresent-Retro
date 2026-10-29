import time
import thumby
import math

# tank game make destructable terrain
# also add planes that can drop bombs
# add aliens that try raiding you
# add levels or procedual generation
# ect. ect.
# add diffecnt textures
# 4 color system
# add more stuff
# like: instructions
# sound
# particles
# ect.
# tank 3 types, helicopter 3 types, plane, granade launcher? limited ammo, supply box drops, ships? foot solderies prob not, aliens 6 types
# tank fast, weak
# medium good range
# heavy slow large projectiles
# nuke drops
# drone contol
# aliens attacking walls
# alians breacking water
# alians making ramp to get over walls
# alian spltter effect
# sync files
# add buring animation with smoke
# python sync files with thumby ide
# maybe make vs code extension
# so i can edit bitmaps
# maybe i only need one way and occasionally copy paste
# add nice start menu
# with buttons for setting up 4 color monochrome
# ect
# this is kinda like ranting idk

# BITMAP: width: 32, height: 32
bitmap0 = bytearray([0,0,0,0,0,0,0,0,248,8,232,40,40,40,40,40,40,40,40,40,40,232,8,248,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,255,0,63,32,32,32,32,32,32,32,32,32,32,63,0,255,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,255,0,12,12,63,63,12,12,0,0,24,24,3,3,0,255,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,31,16,16,16,16,20,18,16,20,18,16,16,16,16,16,31,0,0,0,0,0,0,0,0])


# Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
thumbySprite = thumby.Sprite(32, 32, bitmap0)

thumby.display.setFPS(60)

while(1):
    t0 = time.ticks_ms()   # Get time (ms)
    thumby.display.fill(0) # Fill canvas to black

    bobRate = 250 # Set arbitrary bob rate (higher is slower)
    bobRange = 5  # How many pixels to move the sprite up/down (-5px ~ 5px)

    # Calculate number of pixels to offset sprite for bob animation
    bobOffset = math.sin(t0 / bobRate) * bobRange

    # Center the sprite using screen and bitmap dimensions and apply bob offset
    thumbySprite.x = int((thumby.display.width/2) - (32/2))
    thumbySprite.y = int(round((thumby.display.height/2) - (32/2) + bobOffset))

    # Display the bitmap using bitmap data, position, and bitmap dimensions
    thumby.display.drawSprite(thumbySprite)
    thumby.display.update()


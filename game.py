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
# add 30 levels
# make levels mission based 
# also hackatime got blocked
# lockin with ~3 hours per day
# add more particle effects for shooting
# 16x16 sprites for vehicles
# 8x8 alians 16x16 aliens 32x32 mega aliens
# 4x4 projectiles 2x2 projectiles
# exlosions size of tanks and helicopters 16x16
# nuke explosions
# alians that shoot stuff
# flying alians
# should i have ai bots manning other vehicles?
# oh maybe just have battering rams that dont move and just autofire
# add closest alian to fire
# invisble health bars
# alians and battering rams get destroyed
# stationary walls to keep alians out simulation
# test 2

# redo specs:
# 1. make a destroyable field
# 2. add a little player that can jump around
# 3. add first tank that can shoot and destroy terrain
# 4. add a enemy tank clone
# 5. add more enemies
# 6. add autoaiming
# 7. add a helicopter
# 8. add a plane
# 9. add polish like explosions and sound
# 10. add water
# 11. add ship
# 12. add submarine
# 13. add more polish like a start menu
# 14. add nice readme

# coloring of field will be white background
# black dirt/ dark grey but definitly 2 thick band across top
# destroyable field will have pixles of 100 tall and will have slope of about 1/4 max
# tanks will not be able to go up steep hills and will have to be jumped out off to get past
# enemy tanks will have exact same autoaim technology as you but your health is greatly inflated
# tanks = 12x8
# helicopters = 12x8
# planes = 16x8
# ships = 16x8
# submarines = 16x8
# guy = 2x2


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


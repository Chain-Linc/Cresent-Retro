import framebuf

TRANSPARENT = 15


class Rect:
    def __init__(self, x=0, y=0, w=0, h=0):
        # just like pygame
        # x,y, pos
        # w,h, size
        # top, left, bottom, right
        # topleft, bottomleft, topright, bottomright
        # centerx,centery, center
        # midtop, midleft, midbottom, midright
        self._x = x
        self._y = y
        self._pos = (self._x, self._y)

        self._w = w
        self._h = h
        self._size = (self._w, self._h)

        self._top = self._y
        self._left = self._x
        self._bottom = self._y + self._h
        self._right = self._x + self._w

        self._topleft = (self._left, self._top)
        self._bottomleft = (self._left, self._bottom)
        self._topright = (self._right, self._top)
        self._bottomright = (self._right, self._bottom)

        self._centerx = (self._left + self.right) / 2
        self._centery = (self._top + self._bottom) / 2
        self._center = (self._centerx, self._centery)

        self._midtop = (self._centerx, self._top)
        self._midleft = (self._left, self._centery)
        self._midbottom = (self._centerx, self._bottom)
        self._midright = (self._right, self._centery)

    @property
    def x(self):
        return self.x
    @x.setter
    def x(self, newX):
        oldX = self._x
        self._x = newX

        self._pos = (self._x, self._y)
        self.w = self._w + (newX - oldX)

        self._left = self._x

        self._topleft = (self._left, self._top)
        self._bottomleft = (self._left, self._bottom)

        

        self._midtop = (self._centerx, self._top)
        self._midleft = (self._left, self._centery)
        self._midbottom = (self._centerx, self._bottom)
        self._midright = (self._right, self._centery)

    @property
    def w(self):
        return self._w
    @w.setter
    def w(self, newW):
        self._size = (self._w, self._h)
        self.right = self._x + self._w

    @property
    def right(self):
        return self._w
    @right.setter
    def right(self, newRight):
        self._right = newRight
        
        self._topright = (self._right, self._top)
        self._bottomright = (self._right, self._bottom)

        self._centerx = (self._left + self.right) / 2

# bytes in format c, c, t, t which mean first 2 which are c is for 2bit color then n is for none which means it does nothing then then if all pixles are (n and t) are 1 then pixel is transparent
class Surface:
    def __init__(self, w, h, bytes=None):
        if bytes == None:
            # Fancy negative floor division for ceiling division so I have enough bytes
            bytes = bytearray(-(-(w*h)//2))
        self.surface = framebuf.FrameBuffer(bytes, w, h, framebuf.GS4_HMSB)
        self.w = w
        self.h = h

    def blit(self, blitSurface, x=0, y=0):
        self.surface.blit(blitSurface.surface, x, y, key=TRANSPARENT)

class Sprite:
    def __init__(self, surfaces, x=0, y=0, frame=0):
        self.frame = 0
        self._surface = self.surface
        self.rect = Rect(x, y, self.surface.w, self.surface.h)

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def score(self, value):
        self._surface = value
        

    def on_score_change(self, old, new):
        print(f"Score changed from {old} to {new}!")
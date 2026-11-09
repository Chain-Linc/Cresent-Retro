import framebuf

TRANSPARENT = 15


class Rect:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

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
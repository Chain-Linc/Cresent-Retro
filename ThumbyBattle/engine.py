import framebuf

TRANSPARENT = 15


class Rect:
    def __init__(self, x=0, y=0, w=0, h=0):
        # Note unless directly tied only to width/height it modifies x/y always instead

        # 1st degree varibles use their own varibles
        # base
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # some boiler plate for varibles
    # 2nd degree varibles use 1st degree varibles
    # some useful dual pairs
    @property
    def pos(self):
        return (self.x, self.y)
    @pos.setter
    def pos(self, new):
        self.x, self.y = new

    @property
    def size(self):
        return (self.w, self.h)
    @pos.setter
    def size(self, new):
        self.w, self.h = new

    # all edges
    @property
    def left(self):
        return self.x
    @left.setter
    def left(self, new):
        self.x = new

    @property
    def top(self):
        return self.y
    @top.setter
    def top(self, new):
        self.y = new

    @property
    def right(self):
        return self.x + self.w
    @right.setter
    def right(self, new):
        self.x = new - self.w

    @property
    def bottom(self):
        return self.y + self.h
    @bottom.setter
    def bottom(self, new):
        self.y = new - self.h

    # all centers
    @property
    def centerx(self):
        return (self.x + self.right) / 2
    @centerx.setter
    def centerx(self, new):
        self.x += new - self.centerx

    @property
    def centery(self):
        return (self.y + self.bottom) / 2
    @centery.setter
    def centery(self, new):
        self.y += new - self.centery


    # 3rd degree varibles all use 2nd degree varibles
    @property
    def center(self):
        return (self.centerx, self.centery)
    @center.setter
    def center(self, new):
        self.centerx, self.centery = new

    # all corners
    @property
    def topleft(self):
        return self.pos
    @topleft.setter
    def topleft(self, new):
        self.pos = new

    @property
    def bottomleft(self):
        return (self.x, self.bottom)
    @bottomleft.setter
    def bottomleft(self, new):
        self.x, self.bottom = new

    @property
    def topright(self):
        return (self.right, self.top)
    @topright.setter
    def topright(self, new):
        self.right, self.top = new

    @property
    def bottomright(self):
        return (self.right, self.bottom)
    @bottomright.setter
    def bottomright(self, new):
        self.right, self.bottom = new

    # all mid points
    @property
    def midtop(self):
        return (self.centerx, self.top)
    @midtop.setter
    def midtop(self, new):
        self.centerx, self.top = new
    
    @property
    def midleft(self):
        return (self.left, self.centery)
    @midleft.setter
    def midleft(self, new):
        self.left, self.centery = new
    
    @property
    def midbottom(self):
        return (self.centerx, self.bottom)
    @midbottom.setter
    def midbottom(self, new):
        self.centerx, self.bottom = new
    
    @property
    def midright(self):
        return (self.right, self.centery)
    @midright.setter
    def midright(self, new):
        self.right, self.centery = new

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
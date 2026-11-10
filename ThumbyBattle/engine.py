import framebuf

TRANSPARENT = 15


class Rect:
    def __init__(self, nx=0, ny=0, nw=0, nh=0):
        # just like pygame
        # x,y, pos
        # w,h, size
        # top, left, bottom, right
        # topleft, bottomleft, topright, bottomright
        # centerx,centery, center
        # midtop, midleft, midbottom, midright

        # Note unless directly tied only to width/height it modifies x/y always instead

        # base
        self.x = nx
        self.y = ny

        self.w = nw
        self.h = nh

        # dependent/doesent affect others


        self._midtop = (self._centerx, self._top)
        self._midleft = (self._x, self._centery)
        self._midbottom = (self._centerx, self._bottom)
        self._midright = (self._right, self._centery)

    # some boiler plate

    # 1st degree varibles use their own varibles
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, new):
        self._x = new

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new):
        self._y = new

    @property
    def w(self):
        return self._w
    @w.setter
    def w(self, new):
        self._w = new

    @property
    def h(self):
        return self._h
    @y.setter
    def h(self, new):
        self._h = new

    # 2nd degree varibles use 1st degree varibles
    @property
    def pos(self):
        return (self._x, self._y)
    @pos.setter
    def pos(self, new):
        self._x, self._y = new

    @property
    def size(self):
        return (self._w, self._h)
    @pos.setter
    def size(self, new):
        self._w, self._h = new

    @property
    def left(self):
        return self._x
    @left.setter
    def left(self, new):
        self._x = new

    @property
    def top(self):
        return self._y
    @top.setter
    def top(self, new):
        self._y = new

    @property
    def right(self):
        return self._x + self._w
    @right.setter
    def right(self, new):
        self._x = new - self._w

    @property
    def bottom(self):
        return self._y + self._h
    @bottom.setter
    def bottom(self, new):
        self._y = new - self._h

    @property
    def centerx(self):
        return (self._x + self.right) / 2
    @centerx.setter
    def centerx(self, new):
        self._x += new - self.centerx

    @property
    def centery(self):
        return (self._y + self.bottom) / 2
    @centery.setter
    def centery(self, new):
        self._y += new - self.centery


    # 3rd degree varibles all use 2nd degree varibles
    @property
    def center(self):
        return (self.centerx, self.centery)
    @center.setter
    def center(self, new):
        self.centerx, self.centery = new

    @property
    def topleft(self):
        return self.pos
    @topleft.setter
    def topleft(self, new):
        self.pos = new

    #@property
    #def _(self):
    #    return 
    #@_.setter
    #def _(self, new):
    #    _ = new
    #    self._bottomleft = (self._x, self._bottom)
    #    self._topright = (self._right, self._top)
    #    self._bottomright = (self._right, self._bottom)

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
from ..GAGBasic import *
from ...utils import *
from numpy import array

class GAGLine(GAGBasic):
    def __init__(self, x=0, y=0, x2=10, y2=10):
        super().__init__()
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

        self.width = x2 - x
        self.height = y2 - y
        self.color = "#ffffff"

    def bresenham(self, x0, y0, x1, y1):
        out = []
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2*dy - dx
        y = 0

        for x in range(dx + 1):
            out.append((x0 + x*xx + y*yx, y0 + x*xy + y*yy)) 
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy

        return out
    
    def __str__(self):
        out = ""
        coords = self.bresenham(self.x, self.y, self.x2, self.y2)
        for y in range(self.height+self.y):
            for x in range(self.width):
                if (x, y) in coords: # SHHHHHH don't worry about the big-O notation
                    out += '█'
                else:
                    out += ' '

            out += '\n'

        return hexANSI(self.color) + out.strip()

    def draw(self, x1, y1, x2, y2):
        super().draw(x1, y1, x2, y2)

        self.object = str(self)

        return array(parseObject(self))[y1:y2, x1:x2]
from ..GAGBasic import *
from ...utils import *

from numpy import array

class GAGGraphic(GAGBasic):
    def __init__(self, x=0, y=0, width=1, height=1):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = "#ffffff"

    def draw(self, x1, y1, x2, y2):
        super().draw(x1, y1, x2, y2)
        self.object = (hexANSI(self.color) + (f"█"*self.width + "\n")*self.height).strip()

        return array(parseObject(self))[y1:y2, x1:x2]
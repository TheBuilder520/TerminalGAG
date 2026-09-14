from ..GAGBasic import *
from ...utils import *

class GAGGraphic(GAGBasic):
    def __init__(self, x=0, y=0, width=1, height=1):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = "#ffffff"

    def create(self):
        super().create()
        self.object = hexANSI(self.color) + (f"█"*self.width + "\n")*self.height

    def update(self, elapsed):
        super().update(elapsed)
        self.object = hexANSI(self.color) + (f"█"*self.width + "\n")*self.height
                
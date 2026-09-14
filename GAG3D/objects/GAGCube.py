from ..GAGBasic3D import *
from ...utils import *

class GAGCube(GAGBasic3D):
    def __init__(self, x=0, y=0, z=0, width=10, height=10, depth=10):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
        self.color = "#ffffff"

    def create(self):
        super().create()
        tempObject = []
        for i in range(self.depth):
            tempObject.append(hexANSI(self.color) + (f"█"*self.width + "\n")*self.height)

        self.object = tempObject

    def update(self, elapsed):
        super().update(elapsed)
        tempObject = []
        for i in range(self.depth):
            tempObject.append(hexANSI(self.color) + (f"█"*self.width + "\n")*self.height)

        self.object = tempObject
                
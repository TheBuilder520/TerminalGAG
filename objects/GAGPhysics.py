from ..GAGBasic import *

import math

class GAGPhysics(GAGBasic):
    def __init__(self, x, y, width=None):
        super().__init__()
        self.velocityX = 0
        self.velocityY = 0
        self.friction = 0.01
        self.airResistance = 0.1
        self.decimalY = x
        self.decimalX = y
        self.onGround = False


    def update(self, elapsed):
        self.decimalY += self.velocityY * elapsed
        self.decimalX += self.velocityX * elapsed

        if self.onGround:
            self.velocityX *= self.friction**elapsed
            self.velocityY *= self.friction**elapsed
        else:
            self.velocityX *= self.airResistance**elapsed
            self.velocityY *= self.airResistance**elapsed
            
            

        self.y = math.floor(self.decimalY)
        self.x = math.floor(self.decimalX)
        # print(self.decimalY, self.decimalX)
        super().update(elapsed)

    
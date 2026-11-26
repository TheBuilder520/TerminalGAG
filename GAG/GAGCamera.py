from .objects.GAGText import *
from ..config import *
from ..utils import *
import sys
import os

class GAGCamera:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.screen = GAGI.screen
        self.height = screenHeight
        self.width = screenWidth
        self.viewX = 0
        self.viewY = 0
        self.objectLink = None
        self.linkOffsetX = 0
        self.linkOffsetY = 0
        self.hud = []
        GAGI.cameras.append(self)
        self.create()
        if debug: print(f"camera initialized {self.width}x{self.height}")

    def __str__(self):
        """Returns the camera name"""
        return self.__class__.__name__
    
    def create(self):
        """Ran when the object is first created"""
        if debug: print("camera created")

        if FPSCounter:
            self.GAGfps = GAGText(0, 0, "")
            self.GAGfps.create()
            self.add(self.GAGfps)

        self.screen.create()

    def add(self, object:GAGBasic):
        """Adds an object to the state."""
        object.create()
        self.hud.append(object)

    def draw(self, drawObject):
        # Test to see if the object overlaps the camera, if not, do nothing since it would be a wast to render something you cant see.
        if (drawObject.x <= self.viewX + self.width and drawObject.x + drawObject.width >= self.viewX and drawObject.y <= self.viewY + self.height and drawObject.y + drawObject.height >= self.viewY): 

            x1 = int(max(self.viewX, drawObject.x) - drawObject.x)
            y1 = int(max(self.viewY, drawObject.y) - drawObject.y)

            x2 = int(min(self.viewX + self.width, drawObject.x + drawObject.width) - drawObject.x)
            y2 = int(min(self.viewY + self.height, drawObject.y + drawObject.height) - drawObject.y)

            screenX = round(drawObject.x - self.viewX + x1)
            screenY = round(drawObject.y - self.viewY + y1)

            insertObjectC(screenX, screenY, drawObject.draw(x1, y1, x2, y2), self.screen.screen)

        
    def update(self, elapsed):
        """Ran every frame"""
        for object in self.hud: 
            object.update(elapsed)

            if object.visible:
                parsedObject = parseObject(object)
                insertObject(object, parsedObject, self.screen.screen)
                #if debug: print(parsedObject)
        
        if FPSCounter:
            self.GAGfps.text = "FPS: " + str(round(1/elapsed)) 

            if round(1/elapsed) < 10:
                self.GAGfps.color = "#ff0000"
            elif round(1/elapsed) < FPSLimit/2:
                self.GAGfps.color = "#ffff00"
            else:
                self.GAGfps.color = "#00FF00"

        if self.objectLink != None:
            self.viewX = self.objectLink.x + self.linkOffsetX
            self.viewY = self.objectLink.y + self.linkOffsetY
from ..GAGBasic import *
from ...utils import *
from ...GAGTimer import *

# This will probably be the most useful and most used object

class GAGSprite(GAGBasic):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.FPS = 24
        self.color = "#ffffff"
        self.updateOnColorChange = True
        self.__lastColor = self.color
        self.__animationDict = {}
        self.__graphic = []
        self.currentAnimation = None
        self.__idleAnimation = ""
        self.__numFrames = 0
        self.__currentFrame = 0
        self.__timer = GAGTimer(1/self.FPS)

    def loadGraphic(self, graphicList=[" "]):
        self.__graphic = graphicList
        self.object = hexANSI(self.color) + self.__graphic[0]
        self.width = len(graphicList[0].split("\n")[0])
        self.height = len(graphicList[0].split("\n"))

    def addAnimation(self, animationName="None", frameNumbers=[0], loop=False):
        self.__animationDict.update({animationName:[frameNumbers, loop]})

    def playAnimation(self, animationName:str):
        self.__currentFrame = 0
        self.currentAnimation = animationName
        try: 
            self.object = hexANSI(self.color) + self.__graphic[self.__animationDict[animationName][0][0]]
            self.__numFrames = len(self.__animationDict[animationName][0])
            self.__timer.reset()
        except: self.object = f"{hexANSI("#ff0000")}ERROR!"

        self.width = len(self.object.split("\n")[0])
        self.height = len(self.object.split("\n"))

    def update(self, elapsed):
        super().update(elapsed)
        self.__timer.update(elapsed)

        if self.__lastColor != self.color and self.updateOnColorChange:
            self.object = hexANSI(self.color) + self.__graphic[0]
            self.__lastColor = self.color

        if self.__timer.getLength() != 1/self.FPS: self.__timer.setLength(1/self.FPS)

        if self.__timer.isComplete() and (self.currentAnimation != None):
            self.__currentFrame += 1
            self.__timer.reset()

            self.object = hexANSI(self.color) + self.__graphic[self.__animationDict[self.currentAnimation][0][self.__currentFrame]]

            if self.__currentFrame+1 == self.__numFrames and not self.__animationDict[self.currentAnimation][1]:
                self.currentAnimation = None 

                self.__currentFrame = 0

                if self.__idleAnimation != "":
                    self.playAnimation(self.__idleAnimation)

            if self.__currentFrame+1 == self.__numFrames and self.__animationDict[self.currentAnimation][1]:
                self.__currentFrame = -1

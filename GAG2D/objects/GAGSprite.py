from ..GAGBasic import *
from ...utils import *
from ...GAGTimer import *

class GAGSprite(GAGBasic):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.FPS = 24
        self.__animationDict = {}
        self.__graphic = []
        self.__currentAnimation = None
        self.__totalElapsed = 0
        self.__numFrames = 0
        self.__currentFrame = 0
        self.__timer = GAGTimer(1/self.FPS)

    def loadGraphic(self, graphicList=[" "]):
        self.__graphic = graphicList
        self.width = len(graphicList[0].split("\n")[0])
        self.height = len(graphicList[0].split("\n"))

    def addAnimation(self, animationName="None", frameNumbers=[0]):
        self.__animationDict.update({animationName:frameNumbers})

    def playAnimation(self, animationName):
        self.__currentAnimation = animationName
        try: 
            self.object = self.__animationDict[animationName][0]
            self.__numFrames = len(self.__animationDict[animationName])
            self.__timer.reset()
        except: self.object = f"{hexANSI("#ff0000")}ERROR!"

        self.width = len(self.object.split("\n")[0])
        self.height = len(self.object.split("\n"))

    def update(self, elapsed):
        super().update(elapsed)
        self.__timer.update(elapsed)

        if self.__timer.getLength() != 1/self.FPS: self.__timer.setLength(1/self.FPS)

        if self.__timer.isComplete():
            self.__currentFrame += 1
            self.__timer.reset()
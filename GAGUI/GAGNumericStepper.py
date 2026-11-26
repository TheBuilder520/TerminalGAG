from .GAGBasicUI import *
from ..utils import *
from .styles.roundedStyle import *

from numpy import array

class GAGNumericStepper(GAGBasicUI):
    def __init__(self, x=0, y=0, width=10, selectionX=0, selectionY=0, min=0 ,max=1, increment=1, startingValue=0, text="", style=RoundedStyle()):
        super().__init__()
        self.x = x
        self.y = y
        self.selectionX = selectionX
        self.selectionY = selectionY
        self.width = width
        self.height = 4
        self.text = text
        self.minNum = min
        self.maxNum = max
        self.value = startingValue
        self.increment = increment
        self.__visValue = startingValue
        self.__startValue = startingValue
        self.color = "#ffffff"
        self.style = style
        self.__checkNext = True

    def create(self, state):
        super().create(state)
        self.object = str(self)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)

        if self.selected:
            if self.state.GAGKeyboard.DOWN and self.__visValue > self.minNum:
                self.__visValue -= self.increment
                self.state.playSound("high")
            if self.state.GAGKeyboard.UP and self.__visValue < self.maxNum:
                self.__visValue += self.increment
                self.state.playSound("high")
            if self.state.GAGKeyboard.BACKSPACE:
                self.selected = False
                self.state.inMenu = True
                self.value = self.__startValue
                self.__visValue = self.__startValue
                self.state.playSound("back")
            if self.state.GAGKeyboard.ENTER or self.state.GAGKeyboard.SPACE:
                self.selected = False
                self.state.inMenu = True
                self.__checkNext = False
                self.value = self.__visValue
                self.state.playSound("enter")


    def onSelect(self):
        if self.__checkNext:
            self.selected = True
            self.state.inMenu = False
            self.__startValue = self.value
            self.state.playSound("mid")
        else:
            self.__checkNext = True

    def __str__(self): # I HOPE YOU LIKE F-STRINGS
        if self.selected:
            return f"""{hexANSI(brightness(self.color, 0.5))}{self.text}
{self.style.cornerNW}{self.style.edgeN*(self.width-6)}{self.style.teeN}{self.style.edgeN*5}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{hexANSI(self.color)}{str(self.__visValue)}{hexANSI(brightness(self.color, 0.5))}{self.style.fill*(self.width-7-len(str(self.__visValue)))}{self.style.edgeE}{hexANSI(self.color)} - + {hexANSI(brightness(self.color, 0.5))}{self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-6)}{self.style.teeS}{self.style.edgeS*5}{self.style.cornerSE}"""
        
        elif self.hovering:
            return f"""{hexANSI(self.color)}{self.text}
{self.style.cornerNW}{self.style.edgeN*(self.width-6)}{self.style.teeN}{self.style.edgeN*5}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{str(self.__visValue)}{self.style.fill*(self.width-7-len(str(self.__visValue)))}{self.style.edgeE} - + {self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-6)}{self.style.teeS}{self.style.edgeS*5}{self.style.cornerSE}"""
        
        else:
            return f"""{hexANSI(brightness(self.color, 0.5))}{self.text}
{self.style.cornerNW}{self.style.edgeN*(self.width-6)}{self.style.teeN}{self.style.edgeN*5}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{str(self.__visValue)}{self.style.fill*(self.width-7-len(str(self.__visValue)))}{self.style.edgeE} - + {self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-6)}{self.style.teeS}{self.style.edgeS*5}{self.style.cornerSE}"""

    def draw(self, x1, y1, x2, y2):
        super().draw(x1, y1, x2, y2)

        return array(parseObject(self))[y1:y2, x1:x2]
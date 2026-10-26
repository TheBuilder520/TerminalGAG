from .GAGBasicUI import *
from ..utils import *
from .styles.roundedStyle import *

class GAGDropdown(GAGBasicUI):
    def __init__(self, x=0, y=0, width=10, selectionX=0, selectionY=0, options=["None"], text="", style=RoundedStyle()):
        super().__init__()
        self.x = x
        self.y = y
        self.selectionX = selectionX
        self.selectionY = selectionY
        self.width = width
        self.height = 4
        self.options = options
        self.text = text
        self.selectedText = options[0]
        self.selectedIndex = 0
        self.textColor = "#ffffff"
        self.color = "#ffffff"
        self.style = style
        self.__checkNext = True
        self.__index = 0

    def create(self, state):
        super().create(state)
        self.object = str(self)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)

        self.selectedText = self.options[self.selectedIndex]

        if self.selected:
            self.height = 4 + len(self.options)*2
            if self.state.GAGKeyboard.UP and self.__index > 0:
                self.__index -= 1
                self.state.playSound("high")

            if self.state.GAGKeyboard.DOWN and self.__index < len(self.options)-1:
                self.__index += 1
                self.state.playSound("high")

            if self.state.GAGKeyboard.BACKSPACE:
                self.selected = False
                self.state.inMenu = True
                self.__index = self.selectedIndex
                self.state.playSound("back")

            if self.state.GAGKeyboard.ENTER or self.state.GAGKeyboard.SPACE:
                self.selected = False
                self.state.inMenu = True
                self.__checkNext = False
                self.selectedIndex = self.__index
                self.selectedText = self.options[self.selectedIndex]
                self.state.playSound("enter")

        else:
            self.height = 4
            self.__index = self.selectedIndex


    def onSelect(self):
        if self.__checkNext:
            self.selected = True
            self.state.inMenu = False
            self.state.playSound("mid")
        else:
            self.__checkNext = True

    def __str__(self): # I HOPE YOU LIKE F-STRINGS
        if self.selected:
            header = f"""{hexANSI(self.textColor)}{self.text}
{hexANSI(brightness(self.color, 0.5))}{self.style.cornerNW}{self.style.edgeN*(self.width-5)}{self.style.teeN}{self.style.edgeN*3}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{str(self.selectedText)}{hexANSI(brightness(self.color, 0.5))}{self.style.fill*(self.width-6-len(self.selectedText))}{self.style.edgeE}{hexANSI(self.color)} v {hexANSI(brightness(self.color, 0.5))}{self.style.edgeE}
{self.style.teeW}{self.style.edgeS*(self.width-5)}{self.style.teeS}{self.style.edgeS*3}{self.style.teeE}"""

            items = ""

            for i, item in enumerate(self.options):
                if i == len(self.options)-1:
                    if i == self.__index:
                        items += f"""
{self.style.edgeW}{self.style.fill}{hexANSI(self.color)}{item}{hexANSI(brightness(self.color, 0.5))}{self.style.fill*(self.width-2-len(item))}{self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-1)}{self.style.cornerSE}"""
                    else:
                        items += f"""
{self.style.edgeW}{self.style.fill}{hexANSI(brightness(self.color, 0.5))}{item}{hexANSI(brightness(self.color, 0.5))}{self.style.fill*(self.width-2-len(item))}{self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-1)}{self.style.cornerSE}"""
                else:
                    if i == self.__index:
                        items += f"""
{self.style.edgeW}{self.style.fill}{hexANSI(self.color)}{item}{hexANSI(brightness(self.color, 0.5))}{self.style.fill*(self.width-2-len(item))}{self.style.edgeE}
{self.style.teeW}{self.style.edgeS*(self.width-1)}{self.style.teeE}"""
                    else:
                        items += f"""
{self.style.edgeW}{self.style.fill}{hexANSI(brightness(self.color, 0.5))}{item}{hexANSI(brightness(self.color, 0.5))}{self.style.fill*(self.width-2-len(item))}{self.style.edgeE}
{self.style.teeW}{self.style.edgeS*(self.width-1)}{self.style.teeE}"""

            return header + items
            
        elif self.hovering:
            return f"""{hexANSI(self.textColor)}{self.text}
{hexANSI(self.color)}{self.style.cornerNW}{self.style.edgeN*(self.width-5)}{self.style.teeN}{self.style.edgeN*3}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{str(self.selectedText)}{self.style.fill*(self.width-6-len(self.selectedText))}{self.style.edgeE} v {self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-5)}{self.style.teeS}{self.style.edgeS*3}{self.style.cornerSE}"""
        
        else:
            return f"""{hexANSI(brightness(self.textColor, 0.5))}{self.text}
{hexANSI(brightness(self.color, 0.5))}{self.style.cornerNW}{self.style.edgeN*(self.width-5)}{self.style.teeN}{self.style.edgeN*3}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{str(self.selectedText)}{self.style.fill*(self.width-6-len(self.selectedText))}{self.style.edgeE} v {self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-5)}{self.style.teeS}{self.style.edgeS*3}{self.style.cornerSE}"""
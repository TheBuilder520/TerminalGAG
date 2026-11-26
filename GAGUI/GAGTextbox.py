from .GAGBasicUI import *
from .styles.roundedStyle import *
from ..utils import *

from numpy import array

class GAGTextbox(GAGBasicUI):
    def __init__(self, x=0, y=0, width=10, selectionX=0, selectionY=0, text="", descriptionText="", style=RoundedStyle()):
        super().__init__()
        self.x = x
        self.y = y
        self.selectionX = selectionX
        self.selectionY = selectionY
        self.text = text
        self.descriptionText = descriptionText
        self.__visText = text
        self.width = width
        self.height = 4
        self.color = "#ffffff"
        self.style = style
        self.__checkNext = True
        self.__initText = self.text

    def create(self, state):
        super().create(state)
        self.object = str(self)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)
        #print(self.text)

        if self.selected and GAGI.GAGKeyboard.rawKey != None and GAGI.GAGKeyboard.rawKey not in ["ctrl", "shift", "alt", "caps lock", "windows", "tab", "volume up", "volume down", "volume mute", "print screen", "scroll lock", "pause", "insert", "home", "page up", "page down", "end", "right", "up", "down", "left", "menu", "num lock", "play/pause media", "stop media", "previous track", "next track", "clear", "right ctrl", "right shift", "right alt", "left windows"]:
            key = GAGI.GAGKeyboard.rawKey

            if key == "enter":
                self.selected = False
                self.state.inMenu = True
                self.__checkNext = False
                self.state.playSound("enter")
                return

            if key == "esc":
                self.text = self.__initText
                self.selected = False
                self.state.inMenu = True
                self.state.playSound("back")
                return

            if key == "space":
                key = " "

            if key == "backspace":
                key = ""
                self.text = self.text[:-1]

            if key == "decimal":
                key = "."                

            if key == "delete":
                key = ""
                self.text = ""

            self.text += key
        if self.selected:
            self.__visText = self.text[-self.width+5:] + "█"
        else:
            self.__visText = self.text[-self.width+4:]
            
    def onSelect(self):
        if self.__checkNext:
            self.selected = True
            self.state.inMenu = False
            self.__initText = self.text
            self.state.playSound("mid")
        else:
            self.__checkNext = True


    def __str__(self):
        if self.selected:
            return f"""{hexANSI(brightness(self.color, 0.5))}{self.descriptionText}
{self.style.cornerNW}{self.style.edgeN*(self.width-2)}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{hexANSI(self.color)}{self.__visText}{hexANSI(brightness(self.color, 0.5))}{self.style.fill*(self.width-3-len(self.__visText))}{self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-2)}{self.style.cornerSE}"""
        if self.hovering:
            return f"""{hexANSI(self.color)}{self.descriptionText}
{self.style.cornerNW}{self.style.edgeN*(self.width-2)}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{self.__visText}{self.style.fill*(self.width-3-len(self.__visText))}{self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-2)}{self.style.cornerSE}"""
        else:
            return f"""{hexANSI(brightness(self.color, 0.5))}{self.descriptionText}
{self.style.cornerNW}{self.style.edgeN*(self.width-2)}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{self.__visText}{self.style.fill*(self.width-3-len(self.__visText))}{self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(self.width-2)}{self.style.cornerSE}"""

    def draw(self, x1, y1, x2, y2):
        super().draw(x1, y1, x2, y2)

        return array(parseObject(self))[y1:y2, x1:x2]
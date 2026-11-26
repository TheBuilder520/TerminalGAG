from .GAGBasicUI import *
from .styles.roundedStyle import *
from ..utils import *

from numpy import array

class GAGButton(GAGBasicUI):
    def __init__(self, x=0, y=0, selectionX=0, selectionY=0, text="button", pressFunction=lambda: None, style=RoundedStyle()):
        super().__init__()
        self.x = x
        self.y = y
        self.selectionX = selectionX
        self.selectionY = selectionY
        self.text = text
        self.width = len(self.text)+4
        self.height = 3
        self.pressFunction = pressFunction
        self.color = "#ffffff"
        self.style = style

    def create(self, state):
        super().create(state)
        self.object = str(self)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)

    def onSelect(self):
        self.state.playSound("mid")
        self.pressFunction()

    def __str__(self):
        if self.hovering:
            return f"""{hexANSI(self.color)}{self.style.cornerNW}{self.style.edgeN*(len(self.text)+2)}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{self.text}{self.style.fill}{self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(len(self.text)+2)}{self.style.cornerSE}"""
        else:
            return f"""{hexANSI(brightness(self.color, 0.5))}{self.style.cornerNW}{self.style.edgeN*(len(self.text)+2)}{self.style.cornerNE}
{self.style.edgeW}{self.style.fill}{self.text}{self.style.fill}{self.style.edgeE}
{self.style.cornerSW}{self.style.edgeS*(len(self.text)+2)}{self.style.cornerSE}"""

    def draw(self, x1, y1, x2, y2):
        super().draw(x1, y1, x2, y2)

        return array(parseObject(self))[y1:y2, x1:x2]
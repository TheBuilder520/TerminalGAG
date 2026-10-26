from .GAGBasicUI import *
from ..utils import *
from .styles.roundedStyle import *

class GAGCheckBox(GAGBasicUI):
    def __init__(self, x=0, y=0, selectionX=0, selectionY=0, text="button", style=RoundedStyle()):
        super().__init__()
        self.x = x
        self.y = y
        self.selectionX = selectionX
        self.selectionY = selectionY
        self.text = text
        self.width = len(self.text)+2
        self.height = 1
        self.value = False
        self.style = style
        self.checkColor = "#ffffff"
        self.uncheckColor = "#ffffff"
        self.textColor = "#ffffff"

    def create(self, state):
        super().create(state)
        self.object = str(self)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)

    def onSelect(self):
        if self.value:
            self.value = False
            self.state.playSound("back")
        else:
            self.value = True
            self.state.playSound("enter")

    def __str__(self):
        if self.hovering:
            if self.value:
                return f"""{hexANSI(self.checkColor)}{self.style.check} {hexANSI(self.textColor)}{self.text}"""
            else:
                return f"""{hexANSI(self.uncheckColor)}{self.style.uncheck} {hexANSI(self.textColor)}{self.text}"""
        else:
            if self.value:
                return f"""{hexANSI(brightness(self.checkColor, 0.5))}{self.style.check} {hexANSI(brightness(self.textColor, 0.5))}{self.text}"""
            else:
                return f"""{hexANSI(brightness(self.uncheckColor, 0.5))}{self.style.uncheck} {hexANSI(brightness(self.textColor, 0.5))}{self.text}"""
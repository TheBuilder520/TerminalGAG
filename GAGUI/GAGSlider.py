from .GAGBasicUI import *
from ..utils import *

class GAGSlider(GAGBasicUI):
    def __init__(self, x=0, y=0, width=10, selectionX=0, selectionY=0, min=0 ,max=1, text="button"):
        super().__init__()
        self.x = x
        self.y = y
        self.selectionX = selectionX
        self.selectionY = selectionY
        self.text = text
        self.sliderWidth = width
        self.width = width if len(text) <= width else len(text)
        self.height = 1
        self.value = 0
        self.min = min
        self.max = max
        self.color = "#ffffff"

    def create(self, state):
        super().create(state)
        self.object = str(self)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)

        if self.state.GAGKeyboard.BACKSPACE:
            self.selected = False
            self.state.inMenu = True


    def onSelect(self):
        self.selected = True
        self.state.inMenu = False

    def __str__(self):
        if self.hovering:
            return f"""{hexANSI(self.color)}{'─'*self.sliderWidth} {self.text}"""
        else:
            return f"""{hexANSI(brightness(self.color, 0.5))}{'─'*self.sliderWidth} {self.text}"""
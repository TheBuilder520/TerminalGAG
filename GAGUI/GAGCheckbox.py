from .GAGBasicUI import *
from ..utils import *

class GAGCheckBox(GAGBasicUI):
    def __init__(self, x=0, y=0, selectionX=0, selectionY=0, text="button"):
        super().__init__()
        self.x = x
        self.y = y
        self.selectionX = selectionX
        self.selectionY = selectionY
        self.text = text
        self.width = len(self.text)+2
        self.height = 1
        self.value = False
        self.color = "#ffffff"

    def create(self, state):
        super().create(state)
        self.object = str(self)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)

    def onSelect(self):
        if self.value:
            self.value = False
        else:
            self.value = True

    def __str__(self):
        if self.hovering:
            if self.value:
                return f"""{hexANSI(self.color)}☑ {self.text}"""
            else:
                return f"""{hexANSI(self.color)}☐ {self.text}"""
        else:
            if self.value:
                return f"""{hexANSI(brightness(self.color, 0.5))}☑ {self.text}"""
            else:
                return f"""{hexANSI(brightness(self.color, 0.5))}☐ {self.text}"""
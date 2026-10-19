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
        self.sliderPos = 0
        self.width = width if len(text) <= width else len(text)
        self.height = 1
        self.value = 0
        self.min = min
        self.max = max
        self.color = "#ffffff"
        self.startPosition = 0
        self.__checkNext = True

    def create(self, state):
        super().create(state)
        self.object = str(self)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)

        if self.selected:
            if self.state.GAGKeyboard.BACKSPACE:
                self.selected = False
                self.state.inMenu = True
                self.sliderPos = self.selectPosition
            if self.state.GAGKeyboard.ENTER or self.state.GAGKeyboard.SPACE:
                self.selected = False
                self.state.inMenu = True
                self.__checkNext = False
            if self.state.GAGKeyboard.LEFT and self.sliderPos != 0:
                self.sliderPos -= 1
            if self.state.GAGKeyboard.RIGHT and self.sliderPos != self.sliderWidth:
                self.sliderPos += 1


    def onSelect(self):
        if self.__checkNext:
            self.selected = True
            self.state.inMenu = False
            self.selectPosition = self.sliderPos
        else:
            self.__checkNext = True

    def __str__(self):
        if self.selected:
            return f"""{hexANSI(brightness(self.color, 0.5))}{'─'*self.sliderPos}{hexANSI("#ffffff")}█{hexANSI(brightness(self.color, 0.5))}{'─'*(self.sliderWidth-self.sliderPos)} {self.text}"""
        elif self.hovering:
            return f"""{hexANSI(self.color)}{'─'*self.sliderPos}█{'─'*(self.sliderWidth-self.sliderPos)} {self.text}"""
        else:
            return f"""{hexANSI(brightness(self.color, 0.5))}{'─'*self.sliderPos}█{'─'*(self.sliderWidth-self.sliderPos)} {self.text}"""
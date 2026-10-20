from .GAGBasicUI import *
from ..utils import *
from .styles.roundedStyle import *

class GAGSlider(GAGBasicUI):
    def __init__(self, x=0, y=0, width=10, selectionX=0, selectionY=0, min=0 ,max=1, text="button", style=RoundedStyle()):
        super().__init__()
        self.x = x
        self.y = y
        self.selectionX = selectionX
        self.selectionY = selectionY
        self.text = text
        self.sliderWidth = width
        self.sliderPos = 0
        self.width = width + len(text)
        self.height = 1
        self.minNum = min
        self.maxNum = max
        self.value = (self.maxNum-self.minNum)/self.sliderWidth * (self.sliderPos)
        self.__lastValue = self.value
        self.colorL = "#ffffff"
        self.colorR = "#696969"
        self.colorKnob = "#ffffff"
        self.colorText = "#ffffff"
        self.style = style
        self.selectPosition = 0
        self.__checkNext = True

    def create(self, state):
        super().create(state)
        self.object = str(self)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)

        if self.__lastValue != self.value:
            self.sliderPos = round((self.value * self.sliderWidth) / (self.maxNum - self.minNum))
            self.__lastValue = self.value

        if self.selected:
            if self.state.GAGKeyboard.LEFT and self.sliderPos != 0:
                self.sliderPos -= 1
            if self.state.GAGKeyboard.RIGHT and self.sliderPos != self.sliderWidth:
                self.sliderPos += 1
            if self.state.GAGKeyboard.BACKSPACE:
                self.selected = False
                self.state.inMenu = True
                self.sliderPos = self.selectPosition
            if self.state.GAGKeyboard.ENTER or self.state.GAGKeyboard.SPACE:
                self.selected = False
                self.state.inMenu = True
                self.__checkNext = False
                self.value = (self.maxNum-self.minNum)/self.sliderWidth * (self.sliderPos)


    def onSelect(self):
        if self.__checkNext:
            self.selected = True
            self.state.inMenu = False
            self.selectPosition = self.sliderPos
        else:
            self.__checkNext = True

    def __str__(self): # I HOPE YOU LIKE F-STRINGS
        if self.selected:
            return f"{hexANSI(brightness(self.colorL, 0.5))}{self.style.line*self.sliderPos}{hexANSI(self.colorKnob)}{self.style.knob}{hexANSI(brightness(self.colorR, 0.5))}{self.style.line*(self.sliderWidth-self.sliderPos)} {hexANSI(self.colorText)}{self.text}"
        elif self.hovering:
            return f"{hexANSI(self.colorL)}{self.style.line*self.sliderPos}{hexANSI(self.colorKnob)}{self.style.knob}{hexANSI(self.colorR)}{self.style.line*(self.sliderWidth-self.sliderPos)} {hexANSI(self.colorText)}{self.text}"
        else:
            return f"{hexANSI(brightness(self.colorL, 0.5))}{self.style.line*self.sliderPos}{hexANSI(brightness(self.colorKnob, 0.5))}{self.style.knob}{hexANSI(brightness(self.colorR, 0.5))}{self.style.line*(self.sliderWidth-self.sliderPos)} {hexANSI(brightness(self.colorText, 0.5))}{self.text}"
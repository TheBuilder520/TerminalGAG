from ..GAGBasic import *
from ...utils import *

class GAGText(GAGBasic):
    def __init__(self, x=0, y=0, text=""):
        super().__init__()
        self.text = text
        self.height = 1
        self.x = x
        self.y = y
        self.previousText = ""
        self.color = "#ffffff"


    def create(self):
        super().create()

    def update(self, elapsed):
        self.text = str(self.text)
        self.object = hexANSI(self.color) + self.text

        self.width = trueLen(self.text)
        self.height = len(self.text.split('\n'))

        if self.previousText != self.text:
            self.previousText = self.text

        super().update(elapsed)


from ..GAG2D.GAGBasic import *

class GAGBasicUI(GAGBasic):
    def __init__(self):
        super().__init__()
        self.selectionX = 0
        self.selectionY = 0
        self.selected = False
        self.hovering = False

    def create(self, state):
        self.state = state
        super().create()

    def onHover(self):
        self.hovering = True

    def onSelect(self):
        self.selected = False
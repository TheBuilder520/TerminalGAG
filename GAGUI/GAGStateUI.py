from ..GAG2D.GAGState import *
from .GAGBasicUI import *

class GAGStateUI(GAGState):
    def __init__(self):
        super().__init__()
        self.__selectableItems:list[GAGBasicUI] = []
        self.__buttonPositions:set[tuple[int]] = set()
        self.__selectionX = 0
        self.__selectionY = 0
        self.inMenu = False

    def update(self, elapsed):
        super().update(elapsed)

        for item in self.__selectableItems:
            if item.selectionX == self.__selectionX and item.selectionY == self.__selectionY and item.visible:
                item.onHover()
            else:
                item.hovering = False

        if self.inMenu:
            if self.GAGKeyboard.UP and (self.__selectionX, self.__selectionY-1) in self.__buttonPositions and self.getItem(self.__selectionX, self.__selectionY-1).visible:
                self.__selectionY -= 1

            if self.GAGKeyboard.DOWN and (self.__selectionX, self.__selectionY+1) in self.__buttonPositions and self.getItem(self.__selectionX, self.__selectionY+1).visible:
                self.__selectionY += 1
            # else:
            #     print(self.GAGKeyboard.DOWN, (self.__selectionX, self.__selectionY+1) in self.__buttonPositions, self.getItem(self.__selectionX, self.__selectionY+1).visible)

            if self.GAGKeyboard.LEFT and (self.__selectionX-1, self.__selectionY) in self.__buttonPositions and self.getItem(self.__selectionX-1, self.__selectionY).visible:
                self.__selectionX -= 1

            if self.GAGKeyboard.RIGHT and (self.__selectionX+1, self.__selectionY) in self.__buttonPositions and self.getItem(self.__selectionX+1, self.__selectionY).visible:
                self.__selectionX += 1

            if self.GAGKeyboard.ENTER or self.GAGKeyboard.SPACE:
                for item in self.__selectableItems:
                    if item.selectionX == self.__selectionX and item.selectionY == self.__selectionY and item.visible:
                        item.onSelect()
                    else:
                        item.selected = False

    def getItem(self, x, y, visible=True):
        for item in self.__selectableItems:
            if item.selectionX == x and item.selectionY == y and item.visible == visible:
                return item

    def add(self, object):
        try:
            object.create(self)
            self.__selectableItems.append(object)
            self.__buttonPositions.update({(object.selectionX, object.selectionY)})

        except:
            object.create()

        self.objects.append(object)

    def remove(self, object):
        super().remove(object)
        try:
            self.__selectableItems.remove(object)
            self.__buttonPositions.remove((object.selectionX, object.selectionY))
        except:
            pass
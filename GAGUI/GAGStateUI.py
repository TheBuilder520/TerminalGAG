from ..GAG.GAGState import *
from .GAGBasicUI import *
from pygame import mixer

class GAGStateUI(GAGState):
    def __init__(self):
        super().__init__()
        self.__selectableItems:list[GAGBasicUI] = []
        self.__buttonPositions:set[tuple[int]] = set()
        self.__selectionX = 0
        self.__selectionY = 0
        self.inMenu = False

    def create(self):
        super().create()
        try:
            mixer.init()
            self.audioSupported = True
        except:
            self.audioSupported = False

    def update(self, elapsed):
        super().update(elapsed)

        for item in self.__selectableItems:
            if item.selectionX == self.__selectionX and item.selectionY == self.__selectionY and item.visible:
                item.onHover()
            else:
                item.hovering = False

        if self.inMenu:
            if self.GAGKeyboard.UP:
                if (self.__selectionX, self.__selectionY-1) in self.__buttonPositions and self.getItem(self.__selectionX, self.__selectionY-1):
                    self.__selectionY -= 1
                    self.playSound("low")
                else:
                    self.playSound("denied")

            if self.GAGKeyboard.DOWN:
                if (self.__selectionX, self.__selectionY+1) in self.__buttonPositions and self.getItem(self.__selectionX, self.__selectionY+1):
                    self.__selectionY += 1
                    self.playSound("low")
                else:
                    self.playSound("denied")

            if self.GAGKeyboard.LEFT:
                if (self.__selectionX-1, self.__selectionY) in self.__buttonPositions and self.getItem(self.__selectionX-1, self.__selectionY):
                    self.__selectionX -= 1
                    self.playSound("low")
                else:
                    self.playSound("denied")

            if self.GAGKeyboard.RIGHT:
                if (self.__selectionX+1, self.__selectionY) in self.__buttonPositions and self.getItem(self.__selectionX+1, self.__selectionY):
                    self.__selectionX += 1
                    self.playSound("low")
                else:
                    self.playSound("denied")

            if self.GAGKeyboard.ENTER or self.GAGKeyboard.SPACE:
                for item in self.__selectableItems:
                    if item.selectionX == self.__selectionX and item.selectionY == self.__selectionY and item.visible:
                        item.onSelect()
                    else:
                        item.selected = False

    def destroy(self):
        super().destroy()
        mixer.quit()
    
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

    def playSound(self, name):
        if self.audioSupported:
            match(name):
                case "low": mixer.Sound("./TerminalGAG/sounds/clickLow.wav").play()
                case "mid": mixer.Sound("./TerminalGAG/sounds/clickMid.wav").play()
                case "high": mixer.Sound("./TerminalGAG/sounds/clickHigh.wav").play()
                case "enter": mixer.Sound("./TerminalGAG/sounds/clickEnter.wav").play()
                case "back": mixer.Sound("./TerminalGAG/sounds/clickBack.wav").play()
                case "denied": mixer.Sound("./TerminalGAG/sounds/clickDenied.wav").play()
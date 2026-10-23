from .GAGBasicUI import *
from .styles.roundedStyle import *
from ..utils import *

class GAGBox(GAGBasicUI):
    def __init__(self, x=0, y=0, width=20, height=10, selectionX=0, selectionY=0, tabs=["Box Tab"], style=RoundedStyle()):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selectionX = selectionX
        self.selectionY = selectionY
        self.tabs:list[str] = tabs
        self.__tabObjects = {i:[] for i in self.tabs}
        self.__tabIndex = 0
        self.selectedTab = tabs[0]
        self.color = "#ffffff"
        self.style = style
        self.object = str(self)
        self.__checkNext = True

    def create(self, state):
        super().create(state)

    def update(self, elapsed):
        super().update(elapsed)
        self.object = str(self)

        for tab in self.tabs:
            if tab == self.selectedTab:
                for object in self.__tabObjects[tab]:
                    object.visible = True
            else:
                for object in self.__tabObjects[tab]:
                    object.visible = False

        if self.selected:
            if self.state.GAGKeyboard.LEFT and self.__tabIndex != 0:
                self.__tabIndex -= 1
            if self.state.GAGKeyboard.RIGHT and self.__tabIndex != len(self.tabs)-1:
                self.__tabIndex += 1
            if self.state.GAGKeyboard.BACKSPACE:
                self.selected = False
                self.state.inMenu = True
            if self.state.GAGKeyboard.ENTER or self.state.GAGKeyboard.SPACE:
                self.selected = False
                self.state.inMenu = True
                self.__checkNext = False
                self.selectedTab = self.tabs[self.__tabIndex]

    def addObject(self, tabName, object):
        self.__tabObjects[tabName].append(object)

    def removeObject(self, tabName, object):
        self.__tabObjects[tabName].remove(object)

    def onSelect(self):
        if self.__checkNext:
            self.selected = True
            self.state.inMenu = False
        else:
            self.__checkNext = True

    def __str__(self):
        if self.selected:
            top = ""
            mid = ""
            midMid = ""
            for t in self.tabs:
                top += f"{hexANSI(brightness(self.color, 0.5))}{self.style.cornerNW}{self.style.edgeN*(self.width//len(self.tabs)-2)}{self.style.cornerNE}"

            top += "\n"

            for t in self.tabs:
                mid += f"{hexANSI(brightness(self.color, 0.5))}{self.style.edgeW}{hexANSI(self.color) if t == self.tabs[self.__tabIndex] else ''}{t.center(self.width//len(self.tabs)-2, self.style.fill)}{hexANSI(brightness(self.color, 0.5))}{self.style.edgeE}"

            mid += f"\n{hexANSI(brightness(self.color, 0.5))}"

            for t in self.tabs:
                if t == self.selectedTab:
                    midMid += f"{self.style.cornerSE}{self.style.fill*(self.width//len(self.tabs)-2)}{self.style.cornerSW}"
                else:
                    midMid += f"{self.style.teeS}{self.style.edgeN*(self.width//len(self.tabs)-2)}{self.style.teeS}"

            midMid = (self.style.teeW if midMid[0] != self.style.cornerSE else self.style.edgeW) + midMid[1:-1] + (self.style.teeE if midMid[-1] != self.style.cornerSW else self.style.edgeE)

            bottom =  f"""
{f'{self.style.edgeW}{self.style.fill*(self.width-2)}{self.style.edgeE}\n'*(self.height-4)}{self.style.cornerSW}{self.style.edgeS*(self.width-2)}{self.style.cornerSE}"""

            return top + mid + midMid + bottom
        
        elif self.hovering:
            top = ""
            mid = ""
            midMid = ""
            for t in self.tabs:
                top += f"{hexANSI(self.color)}{self.style.cornerNW}{self.style.edgeN*(self.width//len(self.tabs)-2)}{self.style.cornerNE}"

            top += "\n"

            for t in self.tabs:
                mid += f"{hexANSI(self.color)}{self.style.edgeW}{'' if t == self.selectedTab else hexANSI(brightness(self.color, 0.5))}{t.center(self.width//len(self.tabs)-2, self.style.fill)}{hexANSI(self.color)}{self.style.edgeE}"

            mid += f"\n{hexANSI(self.color)}"

            for t in self.tabs:
                if t == self.selectedTab:
                    midMid += f"{self.style.cornerSE}{self.style.fill*(self.width//len(self.tabs)-2)}{self.style.cornerSW}"
                else:
                    midMid += f"{self.style.teeS}{self.style.edgeN*(self.width//len(self.tabs)-2)}{self.style.teeS}"

            midMid = (self.style.teeW if midMid[0] != self.style.cornerSE else self.style.edgeW) + midMid[1:-1] + (self.style.teeE if midMid[-1] != self.style.cornerSW else self.style.edgeE)

            bottom =  f"""
{f'{self.style.edgeW}{self.style.fill*(self.width-2)}{self.style.edgeE}\n'*(self.height-4)}{self.style.cornerSW}{self.style.edgeS*(self.width-2)}{self.style.cornerSE}"""

            return top + mid + midMid + bottom

        else:
            top = ""
            mid = ""
            midMid = ""
            for t in self.tabs:
                top += f"{hexANSI(brightness(self.color, 0.5))}{self.style.cornerNW}{self.style.edgeN*(self.width//len(self.tabs)-2)}{self.style.cornerNE}"

            top += "\n"

            for t in self.tabs:
                mid += f"{hexANSI(brightness(self.color, 0.5))}{self.style.edgeW}{t.center(self.width//len(self.tabs)-2, self.style.fill)}{hexANSI(brightness(self.color, 0.5))}{self.style.edgeE}"

            mid += f"\n{hexANSI(brightness(self.color, 0.5))}"

            for t in self.tabs:
                if t == self.selectedTab:
                    midMid += f"{self.style.cornerSE}{self.style.fill*(self.width//len(self.tabs)-2)}{self.style.cornerSW}"
                else:
                    midMid += f"{self.style.teeS}{self.style.edgeN*(self.width//len(self.tabs)-2)}{self.style.teeS}"

            midMid = (self.style.teeW if midMid[0] != self.style.cornerSE else self.style.edgeW) + midMid[1:-1] + (self.style.teeE if midMid[-1] != self.style.cornerSW else self.style.edgeE)

            bottom =  f"""
{f'{self.style.edgeW}{self.style.fill*(self.width-2)}{self.style.edgeE}\n'*(self.height-4)}{self.style.cornerSW}{self.style.edgeS*(self.width-2)}{self.style.cornerSE}"""

            return top + mid + midMid + bottom
from copy import deepcopy

from .config import *
from .GAGScreen import *
#from .GAG.GAGState import GAGState
from .GAGKeys import *
import time

class GAGInstanceClass:
    def __init__(self):
        self.screen = GAGScreen()
        self.screen.create()
        self.height = screenHeight
        self.width = screenWidth

        self.cameras = []

        self.GAGKeyboard = GAGKeyboard()

        self.lastState = None
        self.currentState = None
        self.nextState = None
        
        self.inState = False
        self.error = None

        self.elapsed = 0

    def resetCameras(self):
        from .GAG.GAGCamera import GAGCamera
        for cam in self.cameras:
            del cam
            
        self.cameras = [GAGCamera(0, 0, self.width, self.height)]
        self.cameras[0].create()
    
    def startLoop(self):
        if debug: print("starting loop")
        self.resetCameras()
        self.inState = True

        self.currentState.create()

        if customErrors:
            try:
                self.gameLoop()
            except Exception as e:
                self.error = e
                # self.currentState.running = False

                from TerminalGAG.GAGErrorState import ErrorState

                self.nextState = ErrorState(self.error, self.lastState, deepcopy(self.cameras[0].screen.screen))
                self.nextState.create()
                self.gameLoop()

        else:
            self.gameLoop()

        
    def gameLoop(self):
        lastTime = time.time()
        if debug: print("gameLoop")
        while self.currentState.running & (self.currentState != None):
            self.elapsed = time.time() - lastTime
            lastTime = time.time()
            self.update()
            if self.nextState != None:
                self.currentState.destroy()
                self.lastState = self.currentState
                self.currentState = self.nextState
                self.nextState = None
                self.resetCameras()

        self.inState = False
        self.currentState.destroy()
        self.currentState = None

    def update(self):
        self.GAGKeyboard.update(self.elapsed)

        self.screen.screen = self.screen.generateScreen()

        self.currentState.update(self.elapsed)

        for cam in self.cameras:
            cam.update(self.elapsed)

        self.screen.update(self.elapsed)

GAGInstance = GAGInstanceClass()
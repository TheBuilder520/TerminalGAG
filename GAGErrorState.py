from .GAGUI.GAGStateUI import *
from pygame import mixer
from .GAGTween import *
from .GAGTimer import *
from .GAGUI.GAGButton import *
import traceback

class ErrorState(GAGStateUI):
    def __init__(self, error:Exception, lastState, errorVis=[[]]):
        super().__init__()
        lettersASCII = ["""
 _____ 
| ____|
|  _|  
| |___ 
|_____|
""",
r"""
 ____  
|  _ \ 
| |_) |
|  _ < 
|_| \_\
""",
r"""
 ____  
|  _ \ 
| |_) |
|  _ < 
|_| \_\
""",
"""
  ___  
 / _ \ 
| | | |
| |_| |
 \___/ 
""",
r"""
 ____  
|  _ \ 
| |_) |
|  _ < 
|_| \_\
""",
"""
 _ 
| |
| |
|_|
(_)
"""]
        self.error = error
        self.lastState = lastState

        self.errorTitle = GAGText(0, 0, f"")
        self.errorTitle.color = "#ff0000"
        self.totalTime = 0

        self.backgroundImage = ""

        for y in errorVis:
            self.backgroundImage += f"{''.join(y)}\n"

        self.background = GAGText(0, 0, self.backgroundImage)

        self.add(self.background)

        self.letters = []

        for i in range(6):
            object = Letter(screenWidth, screenHeight, i*7, 0.45, lettersASCII[i])
            self.letters.append(object)
            self.add(object)

        self.beat = 0
        self.lastBeat = -1

        self.timerCounter = 0

        self.errorText = GAGText(0, 10, "".join(traceback.format_tb(self.error.__traceback__)) + f"{self.error.__class__.__name__}: {self.error}")
        self.errorText.color = "#C353B8"
        self.errorText.visible = False

        self.exitButton = GAGButton(50, 3, 0, 0, "Exit!", sys.exit)
        self.exitButton.color = "#FF0000"

        if self.lastState != None:
            self.lastStateButton = GAGButton(65, 3, 1, 0, "Return to last state!", self.gotoLastState)
            self.lastStateButton.color = "#FF0000"
            

        self.add(self.errorText)
       
        self.add(self.errorTitle)

        self.inMenu = True

    def gotoLastState(self):
        switchStates(self.lastState)

    def update(self, elapsed):
        super().update(elapsed)
        self.totalTime += elapsed

        if mixer.music.get_busy():
            self.beat = mixer.music.get_pos()//250

        if self.beat != self.lastBeat:
            match(self.beat):
                case 0:
                    if self.audioSupported:
                        mixer.music.load("./TerminalGAG/sounds/Error.wav")
                        mixer.music.play(-1)

                    self.errorTitle.text = "You"

                case 1:
                    self.errorTitle.text = "You got"
                    self.call(self.letters[0].tween)

                case 2:
                    self.errorTitle.text = "You got an "
                    self.call(self.letters[1].tween)

                case 3:
                    self.errorTitle.text = "You got an"
                    self.call(self.letters[2].tween)

                case 4:
                    self.errorTitle.text = "You got an"
                    self.call(self.letters[3].tween)

                case 5:
                    self.errorTitle.text = "You got an"
                    self.call(self.letters[4].tween)

                case 6:
                    self.call(self.letters[5].tween)

                case 8:
                    self.errorText.visible = True
                    self.add(self.exitButton)
                    if self.lastState != None:
                        self.add(self.lastStateButton)

            if self.beat > 8 and self.beat % 2 == 1:
                self.call(self.Flash(self.errorTitle))
                for l in self.letters:
                    self.call(self.Flash(l))

            self.lastBeat = self.beat

        if self.beat > 8:
            for i, l in enumerate(self.letters):
                l.x = (math.sin(self.totalTime*2)*5+(7*i+5))


    class Flash(GAGFunction):   # args: object
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.tweenCounter = 0
            self.startColor = self.args[0].color
            self.args[0].color = "#ffffff"

        def update(self, elapsed):
            super().update(elapsed)
            object = self.args[0]

            self.tweenCounter += 1
            startRGB = hexTuple(self.startColor)
            
            FRAMES = 8
            
            rTween = (255 - startRGB[0])//FRAMES
            gTween = (255 - startRGB[1])//FRAMES
            bTween = (255 - startRGB[2])//FRAMES

            rgb = hexTuple(object.color)
            if rgb[0] > startRGB[0]: r = 255 - rTween*self.tweenCounter
            else: r = startRGB[0]

            if rgb[1] > startRGB[1]: g = 255 - gTween*self.tweenCounter
            else: g = startRGB[1]

            if rgb[2] > startRGB[2]: b = 255 - bTween*self.tweenCounter
            else: b = startRGB[2]

            object.color = f"#{hex(r)[2:].zfill(2)}{hex(g)[2:].zfill(2)}{hex(b)[2:].zfill(2)}"

            if self.tweenCounter >= FRAMES:
                object.color = self.startColor
                self.stop()

class Letter(GAGText):
    def __init__(self, x=0, y=0, finalX=0, tweenTime=0.5, text=""):
        super().__init__(x, y, text)
        self.color = "#ff0000"
        self.tween = GAGTweenObject(self, finalX, 0, "quadIn", tweenTime)


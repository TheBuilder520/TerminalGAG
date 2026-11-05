from .GAGTimer import GAGTimer
from .GAGTween import *

from .utils import *
from .GAG.GAGState import *
from pygame import mixer
from random import randint

VERSION_NUMBER = "2.0.0 Alpha"

def __trueRainbow(text):
    return customGradient(text, ["#ff0000", "#ffff00", "#00ff00", "#00ffff", "#0000ff", "#ff00ff", "#ff0000"])

class SplashScreen(GAGState):
    def create(self):
        super().create()
        self.height = 80
        self.letters:list[Letter] = []
        self.timer = GAGTimer(0.5)
        self.timerCounter = 0
        
        try:
            mixer.init()
            self.audioSupported = True
        except:
            self.audioSupported = False

        for letter in "TerminalGAG":
            object = Letter(randint(0, screenWidth-1), 41, 0.5 if letter != "A" or letter != "G" else 1, letter)
            self.letters.append(object)
            self.add(object)

        if self.audioSupported: 
            mixer.init()
            sound = mixer.Sound("./TerminalGAG/sounds/TerminalGAG Boot.wav")
            mixer.Sound.play(sound)

        self.call(self.timer)
        self.call(self.letters[0].tween)

    def update(self, elapsed):
        super().update(elapsed)
        if self.GAGKeyboard.ENTER:
            self.running = False
            if self.audioSupported: mixer.quit()

        if self.timer.isComplete():
            self.timerCounter += 1
            match(self.timerCounter):
                case 1:
                    self.call(self.letters[1].tween)
                    self.timer.reset()
                case 2:
                    self.call(self.letters[2].tween)
                    self.timer.reset()
                case 3:
                    self.call(self.letters[3].tween)
                    self.timer.reset()
                case 4:
                    self.call(self.letters[4].tween)
                    self.timer.reset()
                case 5:
                    self.call(self.letters[5].tween)
                    self.timer.reset()
                case 6:
                    self.call(self.letters[6].tween)
                    self.timer.reset()
                case 7:
                    self.call(self.letters[7].tween)
                    self.timer.setLength(1)
                    self.timer.reset()
                case 8:
                    self.call(self.letters[8].tween)
                    self.timer.reset()
                case 9:
                    self.call(self.letters[9].tween)
                    self.timer.reset()
                case 10:
                    self.call(self.letters[10].tween)
                    self.timer.setLength(1)
                    self.timer.reset()

                case 11:
                    self.letters[0].tween = GAGTweenObject(self.letters[0], screenWidth//2-6, 20, "sineIn", 0.25)
                    self.letters[0].color = "#ff0000"
                    self.call(self.letters[0].tween)
                    self.timer.setLength(0.25)
                    self.timer.reset()
                case 12:
                    self.letters[1].tween = GAGTweenObject(self.letters[1], screenWidth//2-5, 20, "sineIn", 0.25)
                    self.letters[1].color = "#ff8000"
                    self.call(self.letters[1].tween)
                    self.timer.reset()
                case 13:
                    self.letters[2].tween = GAGTweenObject(self.letters[2], screenWidth//2-4, 20, "sineIn", 0.25)
                    self.letters[2].color = "#ffff00"
                    self.call(self.letters[2].tween)
                    self.timer.setLength(0.125)
                    self.timer.reset()
                case 14:
                    self.letters[3].tween = GAGTweenObject(self.letters[3], screenWidth//2-3, 20, "sineIn", 0.25)
                    self.letters[3].color = "#00ff00"
                    self.call(self.letters[3].tween)
                    self.timer.reset()
                case 15:
                    self.letters[4].tween = GAGTweenObject(self.letters[4], screenWidth//2-2, 20, "sineIn", 0.25)
                    self.letters[4].color = "#00ff80"
                    self.call(self.letters[4].tween)
                    self.timer.setLength(0.25)
                    self.timer.reset()
                case 16:
                    self.letters[5].tween = GAGTweenObject(self.letters[5], screenWidth//2-1, 20, "sineIn", 0.25)
                    self.letters[5].color = "#00ffff"
                    self.call(self.letters[5].tween)
                    self.timer.setLength(0.125)
                    self.timer.reset()
                case 17:
                    self.letters[6].tween = GAGTweenObject(self.letters[6], screenWidth//2, 20, "sineIn", 0.25)
                    self.letters[6].color = "#0080ff"
                    self.call(self.letters[6].tween)
                    self.timer.reset()
                case 18:
                    self.letters[7].tween = GAGTweenObject(self.letters[7], screenWidth//2+1, 20, "sineIn", 0.25)
                    self.letters[7].color = "#0000ff"
                    self.call(self.letters[7].tween)
                    self.timer.setLength(0.25)
                    self.timer.reset()
                case 19:
                    self.letters[8].tween = GAGTweenObject(self.letters[8], screenWidth//2+2, 20, "sineIn", 0.25)
                    self.letters[8].color = "#8000ff"
                    self.call(self.letters[8].tween)
                    
                    self.timer.reset()
                case 20:
                    self.letters[9].tween = GAGTweenObject(self.letters[9], screenWidth//2+3, 20, "sineIn", 0.25)
                    self.letters[9].color = "#ff00ff"
                    self.call(self.letters[9].tween)
                    self.timer.reset()
                case 21:
                    self.letters[10].tween = GAGTweenObject(self.letters[10], screenWidth//2+4, 20, "sineIn", 0.25)
                    self.letters[10].color = "#ff0080"
                    self.call(self.letters[10].tween)
                    self.timer.reset()
                case 22:

                    self.overlayText = GAGText(screenWidth//2-8, 17,                     fr"""
  Powered  by    {hexANSI("#ff0000")}/{hexANSI("#ff8000")}‾{hexANSI("#ffff00")}\{RESET}
˳˳˳˳˳˳˳˳˳˳˳˳˳˳˳˳{hexANSI("#ff00ff")}<{RESET}GAG{hexANSI("#00ff00")}>{RESET}
˳˳˳˳˳˳˳˳˳˳˳˳˳˳˳˳˳{hexANSI("#0080ff")}\{hexANSI("#00ffff")}_{hexANSI("#00ff80")}/{RESET}
  """)
                    self.add(self.overlayText)

                    self.versionText = GAGText(0, screenHeight-1, "Version: " + VERSION_NUMBER)
                    self.add(self.versionText)

                    self.timer.setLength(2)
                    self.timer.reset()

                case 23:
                    self.call(GAGTweenObject(self.overlayText, screenWidth//2-8, -20, "sineIn", 2))
                    self.call(GAGTweenObject(self.versionText, 0, 45, "backIn", 1))

                    for i, letter in enumerate(self.letters):
                        self.call(GAGTweenObject(letter, letter.x, 44, "quadIn", 0.5+(0.1*i)))

                    self.timer.reset()
                case 24:
                    self.running = False
                    


    def destroy(self):
        super().destroy()
        if self.audioSupported: mixer.quit()

class Letter(GAGText):
    def __init__(self, x=0, y=0, tweenTime=0.5, text=""):
        super().__init__(x, y, text)
        self.tween = GAGTweenObject(self, screenWidth//2+0.5, 0, "quadOut", tweenTime)
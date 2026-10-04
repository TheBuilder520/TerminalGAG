# Used to manage all keyboard inputs

import os
import threading
import keyboard
import pyautogui
if os.name != "nt":
    import termios
    import tty
import sys

# TODO add the rest of the keyboard

class GAGKeyboard:
    def __init__(self):
        self.stop = False
        self.keyboardThread = threading.Thread(target=self.keyPress, daemon=True)
        self.keyboardThread.start()
        self.rawKey = None
        
        self.LEFT = False
        self.RIGHT = False
        self.UP = False
        self.DOWN = False
        self.ENTER = False
        self.SPACE = False

        self.A = False
        self.B = False
        self.C = False
        self.D = False
        self.E = False
        self.F = False
        self.G = False
        self.H = False
        self.I = False
        self.J = False
        self.K = False
        self.L = False
        self.M = False
        self.N = False
        self.O = False
        self.P = False
        self.Q = False
        self.R = False
        self.S = False
        self.T = False
        self.U = False
        self.V = False
        self.W = False
        self.X = False
        self.Y = False
        self.Z = False

        if os.name != "posix":
            self.mouseX = 0
            self.mouseY = 0

            self.mouseLeft = False
            self.mouseRight = False
            self.mouseMiddle = False

            self.mouseScroll = 0

    def update(self, elapsed):
        match self.rawKey:
            case "left":
                self.LEFT = True
            case "right":
                self.RIGHT = True
            case "up":
                self.UP = True
            case "down":
                self.DOWN = True
            case "enter":
                self.ENTER = True
            case "space":
                self.SPACE = True
            case "a":
                self.A = True
            case "b":
                self.B = True
            case "c":
                self.C = True
            case "d":
                self.D = True
            case "e":
                self.E = True
            case "f":
                self.F = True
            case "g":
                self.G = True
            case "h":
                self.H = True
            case "i":
                self.I = True
            case "j":
                self.J = True
            case "k":
                self.K = True
            case "l":
                self.L = True
            case "m":
                self.M = True
            case "n":
                self.N = True
            case "o":
                self.O = True
            case "p":
                self.P = True
            case "q":
                self.Q = True
            case "r":
                self.R = True
            case "s":
                self.S = True
            case "t":
                self.T = True
            case "u":
                self.U = True
            case "v":
                self.V = True
            case "w":
                self.W = True
            case "x":
                self.X = True
            case "y":
                self.Y = True
            case "z":
                self.Z = True
            case _:
                self.LEFT = False
                self.RIGHT = False
                self.UP = False
                self.DOWN = False
                self.ENTER = False
                self.SPACE = False

                self.A = False
                self.B = False
                self.C = False
                self.D = False
                self.E = False
                self.F = False
                self.G = False
                self.H = False
                self.I = False
                self.J = False
                self.K = False
                self.L = False
                self.M = False
                self.N = False
                self.O = False
                self.P = False
                self.Q = False
                self.R = False
                self.S = False
                self.T = False
                self.U = False
                self.V = False
                self.W = False
                self.X = False
                self.Y = False
                self.Z = False

        self.rawKey = None

        self.mouseX, self.mouseY = pyautogui.position()

    def keyPress(self):
        from .GAG2D.GAGState import inState # prevents circular imports
        try:
            while inState or not self.stop:
                if os.name == "posix":
                    originalTerminal = termios.tcgetattr(sys.stdin)

                    tty.setcbreak(sys.stdin)
                    
                    key = sys.stdin.read(1)

                    if key == "\033":
                        key += sys.stdin.read(1) 
                        if key[1] != "[":
                            key = "esc"
                        else:
                            key += sys.stdin.read(1)

                    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, originalTerminal)

                    if key == "\033[A": key = "up"
                    elif key == "\033[B": key = "down"
                    elif key == "\033[D": key = "left"
                    elif key == "\033[C": key = "right"
                    elif key == "\n": key = "enter"
                    elif key == chr(127): key = "backspace"
                    elif key == " ": key = "space"

                    self.rawKey = key
                else:
                    key = keyboard.read_event()
                    
                    if key.event_type == keyboard.KEY_DOWN and key.name != None:
                        actualKey = key.name
                        #if actualKey == "enter": input() #prevents accidental command executing
                        if actualKey != None: self.rawKey = actualKey
        except KeyboardInterrupt:
            pass

    def destroy(self):
        self.stop = True
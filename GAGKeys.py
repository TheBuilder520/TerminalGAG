# Used to manage all keyboard inputs

import os
import threading
import keyboard
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
            case _:
                self.LEFT = False
                self.RIGHT = False
                self.UP = False
                self.DOWN = False
                self.ENTER = False
                self.SPACE = False

        self.rawKey = None

    def keyPress(self):
        from .GAGState import inState # prevents circular imports
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
                        if actualKey == "enter": input() #prevents accidental command executing
                        if actualKey != None: self.rawKey = actualKey
        except KeyboardInterrupt:
            pass

    def destroy(self):
        self.stop = True
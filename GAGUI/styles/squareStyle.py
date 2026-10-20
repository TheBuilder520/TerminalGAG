from .templateStyle import *

class SquareStyle(StyleTemplate):
    def __init__(self):
        super().__init__("┌", "┐", "└", "┘", "─", "│", "─", "│", " ", "☑", "☐", "█", "─")

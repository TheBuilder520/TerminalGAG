from .templateStyle import *

class RoundedStyle(StyleTemplate):
    def __init__(self):
        super().__init__("╭", "╮", "╰", "╯", "─", "│", "─", "│", " ", "☑", "☐", "●", "─")

import win32gui
import win32api
import win32con

class TerminalWindow:
    def __init__(self):
        self.window = win32gui.GetForegroundWindow()
        rect = win32gui.GetWindowRect(self.window)
        self.x = rect[0]
        self.y = rect[1]
        self.width = rect[2] - rect[0]
        self.height = rect[3] - rect[1]
        self.screenWidth = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        self.screenHeight = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    def update(self, elapsed):
        rect = win32gui.GetWindowRect(self.window)
        self.x = rect[0]
        self.y = rect[1]
        self.width = rect[2] - rect[0]
        self.height = rect[3] - rect[1]

    def moveWindow(self, x, y):
        win32gui.MoveWindow(self.window, int(x), int(y), self.width, self.height, True)
        self.x = int(x)
        self.y = int(y)

    def resizeWindow(self, width, height):
        win32gui.MoveWindow(self.window, self.x, self.y, int(width), int(height), True)
        self.height = int(height)
        self.width = int(width)

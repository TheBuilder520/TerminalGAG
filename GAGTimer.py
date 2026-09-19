from .GAGFunction import *

class GAGTimer(GAGFunction):
    def __init__(self, length:float):
        super().__init__()
        self.__duration = 0
        self.__length = length

    def update(self, elapsed):
        super().update(elapsed)
        self.__duration += elapsed

    def reset(self):
        self.__duration = 0

    def setLength(self, v:float):
        self.__length = v

    def isComplete(self):
        return self.__duration >= self.__length

    def getDuration(self):
        return self.__duration
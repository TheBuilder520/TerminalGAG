from .GAGFunction import *
import pytweening

class GAGTween(GAGFunction):
    def __init__(self, tweenType="linear", time=1.0, reverse=False):
        super().__init__()
        self.value = 0
        self.__t = 0
        self.__timeToComplete = time
        self.__totalElapsed = 0
        self.__type = self.__getType(tweenType)

        self.reverse = reverse

        if reverse:
            self.__totalElapsed = self.__timeToComplete
            self.value = 1

    def update(self, elapsed):
        super().update(elapsed)
        if (self.__t > 1 and not self.reverse) or (self.__t < 0 and self.reverse):
            return
        if not self.reverse:
            self.__totalElapsed += elapsed
        else:
            self.__totalElapsed -= elapsed

        self.__t = self.__totalElapsed/self.__timeToComplete

        self.value = self.__type(self.__t)

    def reset(self):
        self.__t = 0
        if not self.reverse:
            self.__totalElapsed = 0
            self.value = 0
        else:
            self.__totalElapsed = self.__timeToComplete
            self.value = 1

    def __getType(self, type):
        match(type):
            case "linear":
                return pytweening.linear
            case "sineIn":
                return pytweening.easeInSine
            case "sineOut":
                return pytweening.easeOutSine
            case "sineInOut":
                return pytweening.easeInOutSine
            case "quadIn":
                return pytweening.easeInQuad
            case "quadOut":
                return pytweening.easeOutQuad
            case "quadInOut":
                return pytweening.easeInOutQuad
            case "cubeIn":
                return pytweening.easeInCubic
            case "cubeOut":
                return pytweening.easeOutCubic
            case "cubeInOut":
                return pytweening.easeInOutCubic
            case "quartIn":
                return pytweening.easeInQuart
            case "quartOut":
                return pytweening.easeOutQuart
            case "quartInOut":
                return pytweening.easeInOutQuart
            case "quintIn":
                return pytweening.easeInQuint
            case "quintOut":
                return pytweening.easeOutQuint
            case "quintInOut":
                return pytweening.easeInOutQuint
            case "expoIn":
                return pytweening.easeInExpo
            case "expoOut":
                return pytweening.easeOutExpo
            case "expoInOut":
                return pytweening.easeInOutExpo
            case "circIn":
                return pytweening.easeInCirc
            case "circOut":
                return pytweening.easeOutCirc
            case "circInOut":
                return pytweening.easeInOutCirc
            case "elasticIn":
                return pytweening.easeInElastic
            case "elasticOut":
                return pytweening.easeOutElastic
            case "elasticInOut":
                return pytweening.easeInOutElastic
            case "backIn":
                return pytweening.easeInBack
            case "backOut":
                return pytweening.easeOutBack
            case "backInOut":
                return pytweening.easeInOutBack
            case "bounceIn":
                return pytweening.easeInBounce
            case "bounceOut":
                return pytweening.easeOutBounce
            case "bounceInOut":
                return pytweening.easeInOutBounce
            case _:
                raise TypeError(f"There is no tween called {type}.")
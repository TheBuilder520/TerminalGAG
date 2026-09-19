# Allows a function to get interpreted in the same way an object is by allowing updates on every frame with the downside of not being able to return something easily.

class GAGFunction:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.__running = True

    def create(self):
        """Called when the function is first turned into an object."""
        pass

    def update(self, elapsed):
        """Called on every frame."""
        pass

    def destroy(self):
        self.stop()

    def isRunning(self):
        return self.__running

    def stop(self, returnItem=None):
        self.__running = False
        return returnItem
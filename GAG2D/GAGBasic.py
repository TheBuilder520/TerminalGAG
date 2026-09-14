# This is a basic object that has all the basic attributes apparent on all objects

class GAGBasic:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.visible = True
        self.object = "" # Basically in ASCII art format

    def __str__(self):
        """Returns the object name"""
        return self.__class__.__name__

    def create(self):
        """Called when the object is created"""
        pass

    def update(self, elapsed):
        """Called when the state is updated every frame"""
        pass

    def destroy(self):
        pass
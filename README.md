> [!NOTE]
> TerminalGAG Wiki will be coming in the future.

> [!WARNING]
> Too many objects in one state can cause lag!

# Welcome to TerminalGAG!

TerminalGAG is a package that I am currently working on and actively making changes to. It is not complete so there are probably bugs and other stuff missing, but I plan to make stuff in the future. TerminalGAG uses states and objects to make things work.

## Making your first program with TerminalGAG

We will now be making a hello world program in TerminalGAG.

The first thing you want to do is add ``from TerminalGAG import *`` to the top of your main file.

Then, you would want to create a new file calling it 'PlayState.py'. This file will be your main game.

Inside of your Playstate.py, add these 2 lines of code:

```python
from TerminalGAG.GAG.GAGState import * 
from TerminalGAG.GAG.objects.GAGText import *
```

These 2 lines import the state class and the text object.

Then, add this basic frame work to your file:

```python
class PlayState(GAGState):
  def create(self):
    super().create()

  def update(self, elapsed):
    super().update(elapsed)
```

This will be the start of every state you make.

Next thing you need is a text object. You can do that by adding this line in the create method after the super call.

```python
self.text = GAGText(1, 1, "Hello World!") # The variables are x, y, text
```

Then, you will need to add it to the state with this method.

```python
self.add(self.text)
```

That should be everything you need for your PlayState file.

Now, go back to main, import your PlayState file, and add this function:
```
switchStates(PlayState())
```

You should now be able to run main and get a hello world on the screen!

If you need to change settings, edit the config.py file in the root directory.

# Functions that are useful to help bring TerminalGAG to life

from .config import *

import math
import time
import sys
from copy import deepcopy

from .GAGInstance import GAGInstance as GAGI

RESET = "\033[0m"

def trueLen(text:str):
    """Gives the true length of a string. This will automatically ignore colors and escape codes."""
    out = 0
    skip = False
    for char in text:
        if skip == True and char == "m":
            skip = False
            continue

        if char == "\033":
            skip = True
            continue

        if not skip:
            out += 1

    return out

def hexANSI(hex:str="#000000", foreGround=False): # hex to ANSI
    """Converts a hex code into a color code. (Keep in mind that a true color spectrum is not supported by all systems.)"""
    if hex == "" or hex == " ": return ""
    if hex[0] != "#": raise TypeError("Invalid hex code! Did you perhaps forget a '#'?")
    try:
        r = int(hex[1:3], 16)
        g = int(hex[3:5], 16)
        b = int(hex[5:7], 16)
    except:
        raise Exception(f"Invalid hex code! Expected format '#rrggbb' got '{hex}'.")

    if foreGround:
        return f"\033[48;2;{r};{g};{b}m"
    else:
        return f"\033[38;2;{r};{g};{b}m"

def ANSIHex(ANSI:str="\033[38;2;0;0;0m"):
    """Converts a ANSI escape code into a hex code."""

    ANSI = ANSI.strip("m")
    ANSI = ANSI.split(';')

    r = int(ANSI[-3])
    g = int(ANSI[-2])
    b = int(ANSI[-1])

    return f"#{hex(r)[2:]:2}{hex(g)[2:]:2}{hex(b)[2:]:2}"

def hexTuple(hex:str="#000000"): # hex to ANSI
    """Converts a hex code into a tuple (r, g, b). (Keep in mind that a true color spectrum is not supported by all systems.)"""
    if hex[0] != "#": raise TypeError("Invalid hex code! Did you perhaps forget a '#'?")
    try:
        r = int(hex[1:3], 16)
        g = int(hex[3:5], 16)
        b = int(hex[5:7], 16)
    except:
        raise Exception(f"Invalid hex code! Expected format '#rrggbb' got '{hex}'.")

    return (r, g, b)

def customGradient(text, hex=[]):
    """Returns a string with color codes for gradients."""
    out = []
    colors = [hexTuple(h) for h in hex]
    textLength = len(text)
    colorLength = len(colors)
    splitText = []

    for i in range(colorLength-1):
        splitText.append(text[round(i*(textLength/(colorLength-1))):round((i+1)*(textLength/(colorLength-1)))])

    for i, part in enumerate(splitText):
        for color, letter in enumerate(part):
            r = round((colors[i][0]+((colors[i+1][0]-colors[i][0])/len(part))*color))
            g = round((colors[i][1]+((colors[i+1][1]-colors[i][1])/len(part))*color))
            b = round((colors[i][2]+((colors[i+1][2]-colors[i][2])/len(part))*color))
            out.append(f"\033[38;2;{r};{g};{b}m{letter}")

    out.append("\033[0m")
    return "".join(out)

def parseObject(object) -> list[list[str]]:
    """Converts an object's ASCII art into a 2D Array. You can use '˳' to make transparent pixels."""
    out = []
    skip = False
    activeColor = ""

    splitObject = object.object.split("\n")

    for y, line in enumerate(splitObject):
        out.append([])
        
        for char in line:
            if skip == True:
                activeColor += char
                if char == "m":
                    skip = False
                continue

            if char == "\033":
                skip = True
                activeColor = char
                continue

            if activeColor == RESET:
                activeColor = ""

            if not skip:
                if char == "˳":
                    out[y].append("")
                else:
                    out[y].append(f"{activeColor}{char}{RESET}")
                # print(f"{activeColor}{char}{RESET}")

    #if debug: print("parsed Object")
    #print(out)
    return out

def insertObject(object, parsedObject, plane):
    """Inserts an object into a plane"""

    objectY = math.floor(object.y)
    objectX = math.floor(object.x)
    for y in range(len(parsedObject)):
        for x in range(len(parsedObject[y])):
            try:
                if parsedObject[y][x] != "":
                    plane[(objectY + y) % len(plane)][(objectX + x) % len(plane[0])] = parsedObject[y][x]
            except:
                 plane[(objectY + y) % len(plane)][(objectX + x) % len(plane[0])] = " "

    # print(plane)

    #if debug: print("Inserted Object")

def insertObjectC(x, y, parsedObject, plane):
    """Inserts an object into a plane"""

    objectY = math.floor(y)
    objectX = math.floor(x)
    for y in range(len(parsedObject)):
        for x in range(len(parsedObject[y])):
            try:
                if parsedObject[y][x] != "":
                    plane[(objectY + y) % len(plane)][(objectX + x) % len(plane[0])] = parsedObject[y][x]
            except:
                 plane[(objectY + y) % len(plane)][(objectX + x) % len(plane[0])] = " "

    # print(plane)

    #if debug: print("Inserted Object")

def generatePlane(width, height, fillChar=" "):
    """Generates the physical space objects can appear on"""
    plane = []
    for y in range(height):
        plane.append([])
        for x in range(width):
            plane[y].append(fillChar)
    return plane

def generateSpace(width, height, depth, fillChar=""): # You've heard of 2d arrays before, now may I introduce 3D ARRAYS
    """Generates the physical space objects can appear on"""
    space = [] 
    for z in range(depth):
        space.append([])
        for y in range(height):
            space[z].append([])
            for x in range(width):
                space[z][y].append(fillChar)
    return space

def brightness(hexCode:str = "#ffffff", brightnessMulti=1):
    """Takes a hex code and returns a darker or brighter hex code based on the multiplier. (This is not a constant. This is multiplicative.)"""
    if hexCode == "" or hexCode == " ": return ""
    try:
        r = int(hexCode[1:3], 16)
        g = int(hexCode[3:5], 16)
        b = int(hexCode[5:7], 16)
    except:
        raise Exception(f"Invalid hex code! Expected format '#rrggbb' got '{hex}'.")

    rClamped = max(0, min(round(r*brightnessMulti), 255))
    gClamped = max(0, min(round(g*brightnessMulti), 255))
    bClamped = max(0, min(round(b*brightnessMulti), 255))

    return f"#{hex(rClamped)[2:]:2}{hex(gClamped)[2:]:2}{hex(bClamped)[2:]:2}"

def switchStates(newState):
    from .GAGErrorState import ErrorState
    if debug: print("Switching states")
    GAGI.currentState 
    if not GAGI.inState: # Check to see if a state is already active
        GAGI.currentState = newState
        

        if GAGI.lastState == None:
            GAGI.lastState = deepcopy(newState)

        GAGI.startLoop()

        sys.stdout.write(f"\033[{screenHeight};0H")
    else: # If there is a state already active, destroy it and switch to the new state while trying to use the original switch state function. Prevents nesting states too much
        GAGI.nextState = newState

        GAGI.nextState.create()

        GAGI.error = None

    if GAGI.error != None:
        switchStates(ErrorState(GAGI.error, GAGI.lastState, GAGI.cameras[0].screen.screen))
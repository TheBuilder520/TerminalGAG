# Functions that are useful to help bring TerminalGAG to life

from .config import *

import math

RESET = "\033[0m"

def trueLen(text:str): # TODO Ill work on this later
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

def hexANSI(hex:str="#000000"): # hex to ANSI
    """Converts a hex code into a color code. (Keep in mind that a true color spectrum is not supported by all systems.)"""
    if hex[0] != "#": raise TypeError("Invalid hex code! Did you perhaps forget a '#'?")
    try:
        r = int(hex[1:3], 16)
        g = int(hex[3:5], 16)
        b = int(hex[5:7], 16)
    except:
        raise Exception(f"Invalid hex code! Expected format '#rrggbb' got '{hex}'.")

    return f"\033[38;2;{r};{g};{b}m"

def customGradient(text, colors=[]): # TODO Ill rewrite this later to take hex codes.
    """Returns a string with color codes for gradients."""
    out = []
    textLength = len(text)
    colorLength = len(colors)
    splitText = []

    for i in range(colorLength-1):
        splitText.append(text[round(i*(textLength/(colorLength-1))):round((i+1)*(textLength/(colorLength-1)))])

    for i, part in enumerate(splitText):
        for color, letter in enumerate(part):
            out.append(f"\033[38;2;{round((colors[i][0]+((colors[i+1][0]-colors[i][0])/len(part))*color))};{round((colors[i][1]+((colors[i+1][1]-colors[i][1])/len(part))*color))};{round((colors[i][2]+((colors[i+1][2]-colors[i][2])/len(part))*color))}m{letter}")

    out.append("\033[0m")
    return "".join(out)

def parseObject(object) -> list[list[str]]: # TODO Add color support
    """Converts an object's ASCII art into a 2D Array"""
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
                out[y].append(f"{activeColor}{char}{RESET}")
                # print(f"{activeColor}{char}{RESET}")

    #if debug: print("parsed Object")
    #print(out)
    return out

def insertObject(object, parsedObject, plane):
    """Inserts an object into a plane"""

    objectY = math.floor(object.y)
    objectX = math.floor(object.x)
    for y in range(object.height):
        for x in range(len(parsedObject[0])): # FIX LATER
            plane[(objectY + y) % len(plane)][(objectX + x) % len(plane[0])] = parsedObject[y][x]


    # print(plane)

    #if debug: print("Inserted Object")

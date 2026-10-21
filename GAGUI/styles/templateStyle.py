class StyleTemplate:
    def __init__(self, cornerNW, cornerNE, cornerSW, cornerSE, edgeN, edgeE, edgeS, edgeW, teeN, teeE, teeS, teeW, fill, check, uncheck, knob, line):
        self.cornerNW = cornerNW
        self.cornerNE = cornerNE
        self.cornerSW = cornerSW
        self.cornerSE = cornerSE
        self.edgeN = edgeN
        self.edgeE = edgeE
        self.edgeS = edgeS
        self.edgeW = edgeW
        self.teeN = teeN
        self.teeE = teeE
        self.teeS = teeS
        self.teeW = teeW
        self.fill = fill

        self.check = check
        self.uncheck = uncheck

        self.knob = knob
        self.line = line

    def __str__(self):
        return f"""{self.cornerNW}{self.edgeN}{self.cornerNE}
{self.edgeW}{self.fill}{self.edgeE}
{self.cornerSW}{self.edgeS}{self.cornerSE}"""
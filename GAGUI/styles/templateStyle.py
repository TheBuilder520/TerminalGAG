class StyleTemplate:
    def __init__(self, cornerNW, cornerNE, cornerSW, cornerSE, edgeN, edgeE, edgeS, edgeW, fill):
        self.cornerNW = cornerNW
        self.cornerNE = cornerNE
        self.cornerSW = cornerSW
        self.cornerSE = cornerSE
        self.edgeN = edgeN
        self.edgeE = edgeE
        self.edgeS = edgeS
        self.edgeW = edgeW
        self.fill = fill

    def __str__(self):
        return f"""{self.cornerNW}{self.edgeN}{self.cornerNE}
{self.edgeW}{self.fill}{self.edgeE}
{self.cornerSW}{self.edgeS}{self.cornerSE}"""
class fraction:
    def __init__(self, numer, denom):
        self.numer = numer#numerator
        self.denom = denom#denominator
    def __str__(self):
        return "%s / %s"%(self.numer, self.denom)
class integer:
    def __init__(self, pyNum):
        self.pyNum = int(pyNum)
    def __str__(self):
        return str(self.pyNum)
    def __truediv__(self, i):
        return fraction(self.pyNum, i.pyNum)
    __div__ = __truediv__

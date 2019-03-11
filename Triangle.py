class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def isScalene(self):
        if (self.s1 != self.s2) and (self.s1 != self.s2) and (self.s2 != self.s3):
            return True
        else:
            return False

    def isIsosceles(self):
        if (self.s1 == self.s2) or (self.s1 == self.s3) or (self.s2 == self.s3):
            return True
        else:
            return False

    def isEquilateral(self):
        if (self.s1 == self.s2) and (self.s1 == self.s3):
            return True
        else:
            return False

    def getPerimeter(self):
        return self.s1 + self.s2 + self.s3

    def dilate(self, factor):
        self.s1 *= factor
        self.s2 *= factor
        self.s3 *= factor

    def isCongruent(self, tri2):
        if (self.s1 == tri2.s1) and (self.s2 == tri2.s2) and (self.s3 == tri2.s3):
            return True
        else:
            return False

    def __str__(self):
        return "%s \n\t%s %.1f \n\t%s %.1f \n\t%s %.1f\n" % ("Triangle", "Side 1:", self.s1, "Side 2:", self.s2,
                                                             "Side 3:", self.s3)

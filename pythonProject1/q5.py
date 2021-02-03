class Gps:
    def getChar(self):
        self.s = input()

    def printChar(self):
        print(self.s.upper())

b = Gps()
b.getChar()
b.printChar()
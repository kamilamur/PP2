class StringManipulator:
    def _init_(self):
        self.string = ""
    def getString(self):
        self.string = input("Enter a string: ")
    def printString(self):
        print(self.string.upper())
import random

class Flextextifier(object):
    def __init__(self, uInput):
        self.flextextify(uInput)
    def flextextify(self, uInput):
        input = [character for character in uInput]
        output = ""
        for i in input:
            upperLower = random.randint(0, 1)
            if (upperLower == 0):
                output += i.upper()
            else:
                output += i.lower()
        print(output)

while(True):
    Flextextifier(input("Next query: "))

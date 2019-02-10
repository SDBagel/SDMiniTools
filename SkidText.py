class Skiddifier(object):
    def __init__(self, uInput):
        self.skiddify(uInput)
    def skiddify(self, uInput):
        a = uInput.upper()
        print("***"+((a[0] + "-") * 5), end="")
        for i in range(len(a) - 1):
            print(round(i*1.5)*" " + a[i+1], end="")
        print("!!***")

while(True):
    Skiddifier(input("Next query: "))

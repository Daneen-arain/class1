class myClass:
    __privateVar = 100

    def __privMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        obj.__privMeth()
        print("Private Variable value: ", myClass.__privateVar)

obj = myClass()
try:
    obj.__privMeth()

except:
    obj.hello()
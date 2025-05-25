class Vehicle:
    def drive(self):
        pass

class BMW(Vehicle):
    def drive(self):
        print("BMW is driving smoothly.")

class Ferrari(Vehicle):
    def drive(self):
        print("Ferrari is speeding on the track!")

vehicles = [BMW(), Ferrari()]
for v in vehicles:
    v.drive()

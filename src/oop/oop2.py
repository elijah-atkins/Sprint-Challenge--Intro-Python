# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    #GroundVehicle Constructor creates a new ground vehicle object  that takes num_wheels argument which is set to 4 by default
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels
    #Default drive function prints "vrooom"
    def drive(self):
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    #Constuctor to initialize Motorcycles with 2 wheels
    def __init__(self, wheels=2):
        #using super to call constuctor inside GroundVehicle giving it 2 wheels instead of default 4
        super().__init__(wheels)
    #over rides inherited drive method will return "BRAAAP!!" when called
    def drive(self):
        return "BRAAAP!!"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
for vehicle in vehicles:
    print(f"{vehicle.num_wheels} wheels go {vehicle.drive()}")

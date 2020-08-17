# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# vehicle will be the base class
class Vehicle:
    pass
    # def __init__(self, name, wheels):
    #     self.name = name
    #     self.wheels = wheels
    #
    # def __str__(self):
    #     return f"{self.name} has {self.wheels} wheels."


class FlightVehicle(Vehicle):
    pass
    # def __init__(self, name, wheels, wings):
    #     super().__init__(name, wheels)
    #     self.wings = wings
    #
    # def __str__(self):
    #     return f"{super().__str__()}, and {self.wings} wings."


class Starship(FlightVehicle):
    pass
    # def __init__(self, name, wheels, wings, hyper_speed):
    #     super().__init__(name, wheels, wings)
    #     self.hyper_speed = hyper_speed
    #
    # def __str__(self):
    #     return f"{super().__str__()}, and is able to travel in hyper speed: {self.hyper_speed}"


class Airplane(FlightVehicle):
    pass
    # def __init__(self, name, wheels, wings, speed_of_sound):
    #     super().__init__(name, wheels, wings)
    #     self.speed_of_sound = speed_of_sound
    #
    # def __str__(self):
    #     return f"{super().__str__()}, and is able to break the sound barrier: {self.speed_of_sound}"


class GroundVehicle(Vehicle):
    pass
    # def __init__(self, name, wheels, off_road):
    #     super().__init__(name, wheels)
    #     self.off_road = off_road
    #
    # def __str__(self):
    #     return f"{super().__str__()}, and can travel off road: {self.off_road}"


class Car(GroundVehicle):
    pass
    # def __init__(self, name, wheels, off_road, passengers):
    #     super().__init__(name, wheels, off_road)
    #     self.passengers = passengers
    #
    # def __str__(self):
    #     return f"{super().__str__()} and can carry {self.passengers} passengers."


class Motorcycle(GroundVehicle):
    pass
    # def __init__(self, name, wheels, off_road, saddle_bags):
    #     super().__init__(name, wheels, off_road)
    #     self.saddle_bags = saddle_bags
    #
    # def __str__(self):
    #     return f"{super().__str__()} and has saddle bags: {self.saddle_bags}"

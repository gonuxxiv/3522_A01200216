from Labs.Lab2.vector import Vector
import math


class Asteroid:

    __asteroid_id = 0

    def __init__(self, radius: float, position: Vector, velocity: Vector):
        self.__asteroid_id = Asteroid.__asteroid_id
        Asteroid.__asteroid_id += 1
        self.__circumference = self.calculate_circumference(radius)
        self.__position = position
        self.__velocity = velocity

    def __str__(self):
        return f"Asteroid is currently at {self.get_position()} " \
               f"and moving at {self.get_velocity()} metres per second. " \
               f"It has a circumference of {self.get_circumference()}"

    def get_circumference(self):
        return self.__circumference

    def get_position(self):
        return self.__position.get_coordinates()

    def get_velocity(self):
        return self.__velocity.get_coordinates()

    def get_asteroid_id(self):
        return self.__asteroid_id

    def set_circumference(self, radius):
        self.__circumference = radius

    def set_position(self, position):
        self.__position = position

    def set_velocity(self, velocity):
        self.__velocity = velocity

    @classmethod
    def calculate_circumference(cls, radius):
        return 2 * math.pi * radius

    radius = (get_circumference, set_circumference)

    position = (get_position, set_position)

    velocity = (get_velocity, set_velocity)

    def move(self):
        self.__position.add(self.__velocity)
        return self.__position.get_coordinates()



from Labs.Lab2.vector import Vector
import math


class Asteroid:

    __id = 0

    def __init__(self, radius: int, position: Vector, velocity: Vector):
        """Create a new instance of Asteroid object.

        The function initializes new Asteroid object.

        :param radius: an integer
        :param position: a Vector object
        :param velocity: a Vector object
        :precondition: radius has to be a positive integer; position and velocity have to be Vector objects
        :postcondition: create an Asteroid object
        """
        self.__asteroid_id = Asteroid.__id
        self.increment_id()
        self.__circumference = self.calculate_circumference(radius)
        self.__position = position
        self.__velocity = velocity

    def get_circumference(self) -> float:
        """Get circumference of the asteroid.

        The method returns the circumference of this asteroid.

        :return: circumference of the asteroid as float
        """
        return self.__circumference

    def get_position(self) -> tuple:
        """Get position of the asteroid.

        The method returns the position of this asteroid.

        :return: position of the asteroid as tuple
        """
        return self.__position.get_coordinates()

    def get_velocity(self) -> tuple:
        """Get velocity of the asteroid.

        The method returns the velocity of this asteroid.

        :return: velocity of the asteroid as tuple
        """
        return self.__velocity.get_coordinates()

    def get_asteroid_id(self) -> int:
        """Get asteroid id.

        The method returns the id of this asteroid.

        :return: id of the asteroid as positive integer
        """
        return self.__asteroid_id

    def set_circumference(self, radius: int):
        """Reset circumference of the asteroid.

        The method re-assigns new circumference for this asteroid.

        :param radius: a positive integer
        """
        self.__circumference = radius

    def set_position(self, position: Vector):
        """Reset position of the asteroid.

        The method re-assigns new position for this asteroid.

        :param position: a Vector object
        """
        self.__position = position

    def set_velocity(self, velocity: Vector):
        """Reset velocity of the asteroid.

        The method re-assigns new velocity for this asteroid.

        :param velocity: a Vector object
        """
        self.__velocity = velocity

    @classmethod
    def calculate_circumference(cls, radius: int) -> float:
        """Calculate circumference of the asteroid.

        The method calculates circumference of the asteroid based on given value of the radius.

        :param radius: a positive integer
        :return: circumference value as float
        """
        return 2 * math.pi * radius

    @staticmethod
    def increment_id():
        """Generate new id.

        The method generates new id by incrementing from the previous id value.
        """
        Asteroid.__id += 1

    def move(self) -> tuple:
        """Move asteroid.

        THe method moves the position of the asteroid.

        :return: new position of the asteroid as tuple
        """
        self.__position.add(self.__velocity)
        return self.__position.get_coordinates()

    def __str__(self) -> str:
        """
        Print the object.
        :return: a description of the instance in a formatted string
        """
        return f"Asteroid is currently at {self.get_position()} " \
               f"and moving at {self.get_velocity()} metres per second. " \
               f"It has a circumference of {self.get_circumference()}"


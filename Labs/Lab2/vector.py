class Vector:
    def __init__(self, x: int, y: int, z: int):
        """Create a new instance of Vector object.

        The function initializes new Vector object.

        :param x: a positive int
        :param y: a positive int
        :param z: a positive int
        :precondition: x, y, z have to positive integers
        :postcondition: Create a Vector object
        """
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x_coordinate(self) -> int:
        """Get x value.

        The method returns x value of this Vector.

        :return: value of x as positive int
        """
        return self.__x

    def get_y_coordinate(self) -> int:
        """Get y value.

        The method returns y value of this Vector.

        :return: value of y as positive int
        """
        return self.__y

    def get_z_coordinate(self) -> int:
        """Get z value.

        The method returns z value of this Vector.

        :return: value of z as positive int
        """
        return self.__z

    def set_x_coordinate(self, x: int):
        """Reset x value of the Vector.

        The method re-assigns new x value for this Vector.

        :param x: a positive integer
        """
        self.__x = x

    def set_y_coordinate(self, y: int):
        """Reset y value of the Vector.

        The method re-assigns new y value for this Vector.

        :param y: a positive integer
        """
        self.__y = y

    def set_z_coordinate(self, z: int):
        """Reset z value of the Vector.

        The method re-assigns new z value for this Vector.

        :param z: a positive integer
        """
        self.__z = z

    def add(self, vector):
        """Add vectors.

        The method adds values in the Vector passed as an argument to this Vector.

        :param vector: a Vector object
        """
        self.__x += vector.get_x_coordinate()
        self.__y += vector.get_y_coordinate()
        self.__z += vector.get_z_coordinate()

    def get_coordinates(self) -> tuple:
        """Get x, y, z coordinates of the Vector.

        The method returns x, y, z coordinates of this Vector.

        :return: x, y, z coordinates as tuple
        """
        return self.get_x_coordinate(), self.get_y_coordinate(), self.get_z_coordinate()

    def __str__(self):
        """
        Print the object.
        :return: a description of the instance in a formatted string
        """
        return f"({self.get_x_coordinate()}, {self.get_y_coordinate()}, {self.get_z_coordinate()})"




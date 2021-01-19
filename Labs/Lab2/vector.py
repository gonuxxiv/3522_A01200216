class Vector:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self):
        return f"({self.x_coordinate}, {self.y_coordinate}, {self.z_coordinate})"

    def get_x_coordinate(self):
        return self.__x

    def get_y_coordinate(self):
        return self.__y

    def get_z_coordinate(self):
        return self.__z

    def set_x_coordinate(self, x):
        self.__x = x

    def set_y_coordinate(self, y):
        self.__y = y

    def set_z_coordinate(self, z):
        self.__z = z

    def add(self, vector):
        self.__x += vector.get_x_coordinate()
        self.__y += vector.get_y_coordinate()
        self.__z += vector.get_z_coordinate()

    x_coordinate = (get_x_coordinate, set_x_coordinate)

    y_coordinate = (get_y_coordinate, set_y_coordinate)

    z_coordinate = (get_z_coordinate, set_z_coordinate)

    def get_coordinates(self) -> tuple:
        return self.get_x_coordinate(), self.get_y_coordinate(), self.get_z_coordinate()




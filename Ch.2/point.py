import math


class Point:
    """
    Represents a point in two-dimensional geometric coordinates
    """

    def __init__(self, x=0, y=0):
        """
        Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point default to the origin
        :param x: x position
        :param y: y position
        """
        self.move(x, y)

    def reset(self):
        """
        "reset the point back to the geometric origin: 0, 0
        :return: N/A
        """
        self.x = 0
        self.y = 0

    def move(self, x, y):
        """
        Move the point to a new location in 2D space
        :param x: new x position for Point
        :param y: new y position for Point
        :return: N/A
        """
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second
        :param other_point: second point in which to find
                            the distance from cls.__point__
                            object
        :return: float of distance between the two points
        """
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2
        )


# point1 = Point()
# point2 = Point()
#
# point1.reset()
# point2.move(5, 0)
# print(point2.calculate_distance(point1))
# assert (point2.calculate_distance(point1) ==
#         point1.calculate_distance(point2))
# point1.move(3,4)
# print(point1.calculate_distance(point2))
# print(point1.calculate_distance(point1))
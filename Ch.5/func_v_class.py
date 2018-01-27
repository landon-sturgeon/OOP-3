"""
proficient python programmers use bilut-in data structures unless
(or until) there is an obvious need to define a class.
There is no reason to add an extra level of abstraction if it
doesn't help organize our code. On the other hand, the "obvious"
need is not always self-evident
"""

import math


square = [(1, 1), (1, 2), (2, 2), (2, 1)]


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter


"""
This would require the following calls needed to execute
square = [(1,1), (1,2), (2,2), (2,1)]
perimeter(square)

Seems easy to read but who's to say what a square is, and what the
perimeter function needs in order to function
"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y + p2.y)**2)


# class Polygon(object):
#     def __init__(self):
#         self.vertices = []
#
#     def add_point(self, point):
#         self.vertices.append((point))
#
#     def perimeter(self):
#         perimeter = 0
#         points = self.vertices + [self.vertices[0]]
#         for i in range(len(self.vertices)):
#             perimeter += points[i].distance(points[i+1])
#         return perimeter


"""
for this to run we need the following
square = Polygon()
square.add_point(Point(1,1))
square.add_point(Point(1,2))
square.add_point(Point(2,2))
square.add_point(Point(2,1))
square.perimeter()
Twice as much, but much more readable as we now know square
represents a polygon, which needs a series of Point classes
in order for perimeter() to run correctly. More self documenting
than the function version despite the 2x length in execution code
needed 
"""

"""
code length != good indicator of code complexity
sometimes, one line code that do everything can be more confusing
than a series of lines of code
We can also change the Polygon class above to make it more succinct
"""


class Polygon(object):
    def __init__(self, points=None):
        points = points if points else []
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter

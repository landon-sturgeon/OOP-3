"""
list are the least object-oriented of python's data structures

don't use lists for collecting different attributes of individual items

what we want to avoid is a list of properties a particular shape has such as
['a', 1, 'b', 3]. You'd have to use some weird logic to extract every
other grouping
"""

"""
sorting lists --

list of tuples are sorted with sort() method by first element of each
tuple
if elements in array are of different types, TypeError will be raised

objects can be sorted with a little bit more work
__lt__ which stands for "less than" should be defined on the class to make
instances of that class comparable

the sort method on list will access this method on each object
to determine where it goes in the list. Should return True/False depending
on the logic of how the method handles the passed argument to figure out
if the class is less than the passed argument
"""


class WeirdSortee(object):
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)


"""
__repr__ method makes it easy to see the two values when we print a list

__gt__ == "greater than"
__eq__ == "equal to"
__ne__ == "not equal to"
__ge__ == "greater than or equal to"
__le__ == "less than or equal to"
all these can be used instead of just __lt__

@total_ordering decorator can be used to supply the above functionality
change the above function to use __eq__ would be:
"""

@total_ordering
class WeirdSortee(object):
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)

    def __eq__(self, object):
        return all((
            self.string == object.string,
            self.number == object.number,
            self.sort_num == object.number
        ))


"""
there are a few sort key operations that are so common that the Python
team has supplied them so you don't have to write them yourself
operator.itemgetter() can be used to do this:
"""


from operator import itemgetter

l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
l.sort(key=itemgetter(1))

"""
would sort by the second value of the supplied tuples
"""

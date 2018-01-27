"""
the property function can be used with the decorator syntax to
turn a get function into a property
"""

"""
can specify a setter function for the new property as follows
"""


class Foo(object):
    # this is the getter method
    # the property function returns an object; this object
    # always comes with its own setter attribute, which
    # can the be applied as a decorator to other functions
    @property
    def foo(self):
        return self._foo

    # this is the setter method
    @foo.setter
    def foo(self, value):
        self._foo = value


"""
Using the same name for the get and set methods is not required,
but it does help group the multiple methods that access one
property together
"""


class Silly(object):

    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly")
        del self._silly

"""
WHEN TO USE PROPERTIES

typical use case is the one above; we have some data on a class
that we later want to add behavior to

Technically, data properties and methods are all attributes on a
class
"""

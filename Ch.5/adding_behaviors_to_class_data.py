"""
Python doesn't really have any private attributes or properties
other languages like java do, meaning that they can designate
which properties or attributes can't be touched by public API's
Typically this means that functions are needed in order to change
the value of attributes if ever needed
"""


class Color(object):
    def __init(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


"""
Python favors the direct access verions to attributes
"""


class Color(object):
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name


"""
Implementation would be:
c = Color("#ff0000", "bright red")
print(c.name)
c.name = "red"
"""

"""
Python gives us the property keyword to make methods look like
attributes. We can therefore write our code to use direct member
access, and if we unexpectedly need to alter the implementation
to do some calculation when getting or setting that attribute's
value, we can do so without changing the interface
"""


class Color(object):
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)

"""
the difference between the class above and the one right here
is that the name property now calls both methods, running validation
to make sure that the name is valid

the biggest, most awesome fact about this change is that if we had
code that had directly accessed the name attribute, rather than
setting it through the _set_name() method, the previous code
would still work! no matter how you set the name method now, the
code will work assuming that "" is not passed of course
"""

"""
The best way to think of the property function is a function
returning an object that proxies any requests to set or access
the attribute value through the methods we have specified.
It's like a constructor for such an object and that object is
set as the public facing member for the given attribute
"""


class Silly(object):
    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly

    silly = property(_get_silly, _set_silly,
                     _del_silly, "This is a silly property")

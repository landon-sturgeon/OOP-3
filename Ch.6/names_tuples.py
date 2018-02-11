from collections import namedtuple

Stock = namedtuple("Stock", "symbol current high low")

stock = Stock("FB", 75.00, high=75.03, low=74.90)

"""
dictioanries have the ability to set default key to values if they are not present!
"""

stocks = {}

stocks. setdefault("GOOG", "INVALID")

stocks.setdefault("BBRY", (10.50, 10.62, 10.39))

stocks["BRRY"] # will return (10.50, 10.62, 10.39)

"""
objects that are hashable basically have a defined algorithm that converts the object into a unique 
integer value for rapid lookup. This hask is what is actually used to look up values in a dictionary
"""

"""
defaultdict is useful for creating dictionaries of containers.pass in the object that you want created with a
key in the dictionary is not present (int, list, custom class etc) for the default object in defaultdict, and whenever
you add anything to that dict, make sure the data passed matches the use case of the default object of the defaultdict
"""


from collections import defaultdict


def letter_frequency(sentence):
    frequencies = defaultdict(int)

    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return num_items, {}

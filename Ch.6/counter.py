"""
the need to count specific instances in an iterable use case is common enough that the Python
developers created a spcific class for it
"""


from collections import Counter


def letter_frequency(sentence):
    return Counter(sentence)

"""
most useful method on Counter is the most_common(), which returns a list of (key, count) tuples ordered
by the count. You can pass in an integer argument to get only the top most common elements
"""

responses = {
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "vanilla",
}

print(
    "The children voted for {} ice cream".format(
        Counter(responses).most_common(1)[0][0]
    )
)

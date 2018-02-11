"""
comes from mathematics, where a set is a group of unordered items
we can add a number to a set 5 times, but would only be set once

can hold any hashable object. Because keys have to be unique, and
dictionaries cannot be used as key's (or else they could potentially
lose their unique hash) lists and dictionaries are out
"""


song_library = [("Phantom Of The Opera", "Sarah Brightman"),
                ("Knocking on Heaven's Door", "Guns N Roses"),
                ("Captain Nemo", "Sarah Brightman"),
                ("Patterns in the Sky", "Opeth"),
                ("November Rain", "Guns N Roses"),
                ("Beautiful", "Sarah Brightman"),
                ("Mal's Song", "Vixy and Tony")]

artists = set()
for son, artist in song_library:
    artists.add(artist)

print(artists)

"""
sets like dictioanries are unordered. Both use an underlying hash-based
data structure for efficiency. Because of this you can't look things up
by indexing

Primary purpose is to divide the items in the set by "things that are in
the set" and "things that are not in the set"

While the primary feature of a set in uniqueness, that is not its
primary purpose. Sets are most useful when two or more of them are
used in combination. Most of the operations that sets have are meant
to operate on other sets such as union, intersection, 
symmetric_difference

union = takes a second set as a parameter and returns a new set that
contains all elements that are in either of the two sets (can use "|")

intersection = accepts a second set and returns a new set that contains
only those elements that  are in both sets (can use "&")

symmetric_difference = it is the set of objects that are in one set or
the other, but not both

issubset == returns True if all of the items in the calling set are also
in the set passed as an argument

issuperset == returns True if all of the items in the argument are also
in the calling set

difference == returns all the elements that are in the calling set but
not in the set passed as an argument
"""

"""
queues are peculiar data structures because like sets their functionality
can be handled entirely using lists, but can handle larger data sets
more efficiently (millions of elements vs thousands for lists)

lists are also slow if you're adding elements into a specific location
rather than at the end, and for checking if an element exists in the list
"""

"""
FIFO QUEUE

First in First out

Queue() class represent FIFO
typically used when one object is creating data and one other object is
consuming said data in some way, probably at a different rate

primary methods are put() and get() which adds an element to the back of
the queue or returns the first element in the queue

will block until the queue object has data or room available to complete
the operation. can waive this functionality by passing optional argument
block=False, or wait a defined amount of time before raising an exception
by passing timeout=(int)

also has methods empty() and full()

queues builds on top of python's collections.deque (double ended queue)
for more efficient access to both ends of the collection
"""

"""
LIFO QUEUE

Last in First out

more frequently called stacks

traditionally uses put() and get() like Queue() method, but they return
the first element in the stack or put and element at the first position
of the stack respectively

called using LifoQueue()

typically used with concurrent threading
"""

"""
Priority Queues

uses get() and put() methods as well but returns the most "important" 
items

most important is found by assigning elements in the queue as value
and running the __lt__ or similar options against it

most common is storing two element tuples using the first element in the
tuple to assign level of importance

you can have multiple elements with the same priority but no guarantee
of which one will be returned
"""



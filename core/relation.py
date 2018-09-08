"""
Defines the basic relation abstraction in the interpreter
"""

import string
import random

class Relation(object):

    #each attribute is a hashable type
    def __init__(self, *argv):

        #set of attributes
        self.attributes = set([v for v in argv])

        #initialize the data to be empty
        self.data = []

        #random name
        self.name = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    def setName(self, name):
        self.name = name

    #adds a tuple to the dataset
    def put(self, tup):
        self.data.append(tup)

    #puts all of the data in a dataset
    def putAll(self, data):
        self.data = data

    #replaces a tuple at a particular attribute value
    def update(self, i, attr, value):
        self.data[i][attr] = value

    #replaces a tuple at a particular attribute value
    def updateAppend(self, i, attr, value):
        if attr not in self.data[i]:
            self.data[i][attr] = set()

        self.data[i][attr].add(value)

    #gets an iterator interface over tuples (ref to the base rel, tid, and tuple)
    def get(self):
        for tid , tup in enumerate(self.data):
            yield ([self], [tid], tup)


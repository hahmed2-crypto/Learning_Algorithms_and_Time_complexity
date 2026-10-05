class Node:

    """ an object for storing a single node of linked list.
       Models two attributes - data and the link to the next node in the list
    """
    date=None
    next_node= None
    def __init__(self, data):
        self.data=data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class Linkedlist:
    def __init__(self):
        self.head= None  
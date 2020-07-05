""" Implementation of Circular Queue using Python lists """

class CircularQueue:
    """ Circular Queue is a linear data structure in which the operations are performed based on FIFO
        (First In First Out) principle and the last position is connected back to the first position
        to make a circle. It is also called ‘Ring Buffer’. """

    def __init__(self, maxSize = 100):
        self.queue = [None] * self.maxSize
        self.front = None
        self.rear = None
        self.maxSize = maxSize

    def __str__(self):
        return [self.queue[item] for item in range(self.rear%self.maxSize, self.front%self.maxSize)]

    def __eq__(self, value):
        return self.queue == value.queue and self.maxsize == value.maxsize

    def __len__(self):
        return len(self.queue)

    def __contains__(self, item) -> bool:
        """ Check if an item is in the queue. """
        return item in self.queue

    def __dir__(self):
        return ['__init__', '__str__', '__eq__', '__len__', '__contains__', '__dir__',
                'enqueue', 'dequeue', 'isempty', 'isfull', 'clear', 'getFront', 'getRear']

    def enqueue(self):
        """ add an element in the rear of the queue """
        if self.isfull():
            return False
        else:
            pass

    def dequeue(self):
        """ retrieves and removes the front of the queue, or returns null if this queue is empty. """
        if self.isempty():
            return None
        else:
            d = self.queue[self.front]
            self.queue[self.front%self.maxSize] = None
            self.front = (self.front + 1) % self.maxSize
            return d

    def getFront(self):
        """ Gets the element at the front of the queue without removing it. """
        if self.front is None:
            return None
        else:
            return self.queue[self.front%self.maxSize]

    def getRear(self):
        """ Gets the element at the rear of the queue without removing it. """
        if self.rear is None:
            return None
        else:
            return self.queue[self.rear%self.maxSize]

    def isfull(self):
        """ Checks if the queue is full."""

    def isempty(self):
        """ Checks if the queue is empty. """

    def clear(self):
        """ Removes all elements from the queue."""
        self.queue = [None] * self.maxSize
        self.front = None
        self.rear = None

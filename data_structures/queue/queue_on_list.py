"""Queue represented by a Python list"""


class Queue:
    """ A Queue is a linear structure which follows a particular order in which the operations
        are performed. The order is First In First Out (FIFO). A good example of a queue is any
        queue of consumers for a resource where the consumer that came first is served first.
        The difference between stacks and queues is in removing. In a stack we remove the item
        the most recently added; in a queue, we remove the item the least recently added."""

    def __init__(self, maxsize=100):
        self.queue = list()
        self.maxsize = maxsize

    def __str__(self):
        return  str(self.queue)

    def __eq__(self, value):
        return self.queue == value.queue and self.maxsize == value.maxsize

    def __len__(self):
        return len(self.queue)

    def __contains__(self, item) -> bool:
        """ Check if an item is in the queue. """
        return item in self.queue

    def __dir__(self):
        return ['__init__', '__str__', '__eq__', '__len__', '__contains__', '__dir__',
                'enqueue', 'dequeue', 'isempty', 'isfull', 'clear', 'get_front', 'get_rear']


    def enqueue(self, element):
        """ enqueue an element to the rear of the queue
            params: element, queue """
        if len(self) >= self.maxsize:
            raise QueueOverflowError()
        self.queue.insert(0, element)

    def dequeue(self):
        """ dequeue an element of the font of the queue
            params: queue
        """
        try:
            return self.queue.pop()
        except IndexError as e:
            print("Error: "+str(e))

    def isfull(self):
        """ Checks if the queue is full. """
        return len(self) == self.maxsize

    def isempty(self):
        """ Checks if the queue is empty. """
        return len(self.queue) == 0

    def clear(self):
        """ Removes all elements from the queue."""
        self.queue.clear()

    def get_front(self):
        """ Returns the element at the font of the queue without removing it. """
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[-1]

    def get_rear(self):
        """ Returns the element at the rear of the queue without removing it. """
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

class QueueOverflowError(BaseException):
    def __str__(self):
        return "the maxsize of the queue is excited!"

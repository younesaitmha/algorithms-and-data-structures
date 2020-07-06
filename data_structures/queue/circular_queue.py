""" Implementation of Circular Queue using Python lists """

class CircularQueue:
    """ Circular Queue is a linear data structure in which the operations are performed based on FIFO
        (First In First Out) principle and the last position is connected back to the first position
        to make a circle. It is also called ‘Ring Buffer’. """

    def __init__(self, maxSize = 100):
        self.maxSize = maxSize
        self.queue = [None]*self.maxSize
        self.front = 0
        self.rear = -1
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return str("queue is empty!")
        else:
            l = list()
            index = self.rear
            for i in range(self.size):
                l.append(self.queue[index])
                index = (index + 1)%self.maxSize
            return str(l)

    def __eq__(self, value):
        return self.queue == value.queue and self.maxSize == value.maxSize

    def __len__(self):
        return len(self.size)

    def __contains__(self, item) -> bool:
        """ Check if an item is in the queue. """
        return item in self.queue

    def __dir__(self):
        return ['__init__', '__str__', '__eq__', '__len__', '__contains__', '__dir__',
                'enqueue', 'dequeue', 'isempty', 'isfull', 'clear', 'getFront', 'getRear']

    def enqueue(self, element):
        """ add an element in the rear of the queue """
        if self.isfull():
            raise Exception('queue is full!')
        else:
            self.rear = (self.rear + 1)%self.maxSize
            self.queue[self.rear] = element
            self.size += 1
            return True

    def dequeue(self):
        """ retrieves and removes the front of the queue, or returns null if this queue is empty. """
        if self.isempty():
            raise Exception('queue is empty!')
        else:
            d = self.queue[self.front]
            self.front = (self.front + 1) % self.maxSize
            self.size -= 1
            return d

    def getFront(self):
        """ Gets the element at the front of the queue without removing it. """
        if self.size == 0:
            return None
        return self.queue[self.front%self.maxSize]

    def getRear(self):
        """ Gets the element at the rear of the queue without removing it. """
        if self.size == 0:
            return None
        return self.queue[self.rear%self.maxSize]

    def isfull(self):
        """ Checks if the queue is full."""
        if self.size == self.maxSize:
            return True
        return False


    def isempty(self):
        """ Checks if the queue is empty. """
        if(self.size == 0):
            return True
        return False

    def clear(self):
        """ Removes all elements from the queue."""
        self.queue = [None] * self.maxSize
        self.front = None
        self.rear = None
        self.size = 0


if __name__ == "__main__":
    q = CircularQueue(5)
    q1 = CircularQueue(5)
    q.enqueue(1)
    q.enqueue(0)
    q.enqueue(8)
    q.enqueue(1)
    q.enqueue(5)
    print(q)
    print(q.getRear())
    print(q.getFront())
    q.dequeue()
    print(q)
    print(q.getRear())
    print(q.getFront())


class Stack:
    """ A stack is an abstract data type that serves as a collection of
        elements. Stack is a linear data structure which follows a
        particular order in which the operations are performed. The order
        is LIFO(Last In First Out).
    """

    def __init__(self, maxsize=100):
        self.stack = []
        self.maxsize = maxsize

    def __str__(self):
        return str(self.stack)

    def __eq__(self, value):
        return self.stack == value.stack and self.maxsize == value.maxsize

    def __len__(self):
        return len(self.stack)

    def __contains__(self, item) -> bool:
        """ Check if an item is in the stack """
        return item in self.stack

    def __dir__(self):
        return ['__init__', '__str__', '__eq__', '__len__', '__contains__', '__dir__', 'push',
                'pop', 'is_empty', 'peek', 'clear']

    def push(self, element):
        """ Push an element to the top of the stack
            params: element, stack
        """
        if len(self) >= self.maxsize:
            raise StackOverflowError()
        self.stack.append(element)

    def pop(self):
        """ Pop an element off of the top of the stack
            params: stack
        """
        try:
            return self.stack.pop()
        except IndexError as e:
            print("Error: "+str(e))

    def is_empty(self):
        """ checks if the stack is empty """
        if len(self):
            return True
        else:
            return False

    def peek(self):
        """ Returns the element at the top of the Stack without removing it. """
        try:
            return self.stack[-1]
        except IndexError as e:
            print('IndexError: '+str(e))
            return None

    def clear(self):
        """ Removes all objects from the Stack."""
        self.stack.clear()

class StackOverflowError(BaseException):
    def __str__(self):
        return "the maxsize of the stack is excited!"

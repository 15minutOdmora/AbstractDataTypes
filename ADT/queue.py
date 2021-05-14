class Elt:
    def __init__(self, data: any, dummy: bool = False):
        self.dummy = dummy
        if not dummy:
            self.data = data


class Queue:
    def __init__(self, initial_data):
        self.front = Elt(None, dummy=True)
        self.end = self.front
        if initial_data:
            for elt in initial_data:
                self.enqueue(elt)

    def empty(self) -> bool:
        """
        Method checks if stack is empty
        :return: True/False
        """
        return self.front.dummy

    def enqueue(self, element) -> None:
        """
        Method adds an element to the queue
        :return: None
        """
        self.end.next = Elt(None, dummy=True)
        self.end.data = element
        self.end.dummy = False
        self.end = self.end.next

    def front(self) -> any:
        """
        Returns the first element at the front of the queue.
        :return: Element
        """
        if self.empty():
            raise ValueError("front: The queue is empty.")
        return self.front

    def dequeue(self) -> None:
        """
        Removes the first element from the queue.
        :return: None
        """
        if self.empty():
            raise ValueError("dequeue: The queue is empty.")
        self.front = self.front.next

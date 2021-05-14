class Knot:
    """
    Class representing a knot holding data and a link to the next knot.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    Class representing a linked list.
    """
    def __init__(self):
        self._length = 0
        self._start = None
        self._end = None

    def insert_at_start(self, element) -> None:
        """
        Method inserts and element at the start of the chain
        :param element: any
        :return:int
        """
        if self._start is None:
            knot = Knot(element)
            self._start = knot
            self._end = knot
        else:
            knot = Knot(element, self._start)
            self._end = knot
        self._length += 1

    def insert_at_end(self, element) -> None:
        """
        Method inserts an element at the end of the chain.
        :param element: any
        :return: None
        """
        if self._start is None:
            knot = Knot(element)
            self._start = knot
            self._end = knot
        else:
            end = self._end
            new_end = Knot(element)
            end.next = new_end
            self._end = new_end
        self._length += 1

    @property
    def start(self) -> any:
        """
        Method returns the element at the start of the list.
        :return: any
        """
        if self._start is None:
            raise IndexError("start: Linked chain is empty.")
        return self._start.data

    @property
    def end(self) -> any:
        """
        Method return the element at the end of the linked list.
        :return: any
        """
        if self._start is None:
            raise IndexError("end: Linked chain is empty.")
        return self._end.podatek

    def delete_start(self) -> None:
        """
        Method deletes the element at the start of the linked list.
        :return: None
        """
        if self._start is None:
            raise IndexError("delete_start: Linked list is empty")
        elif self._start == self._end:
            self._start = None
            self._end = None
        else:
            knot = self._start
            new = knot.next
            self._start = self._start.naslednji
        self._length -= 1

    def delete_end(self) -> None:
        """
        Method deletes the element at the end of the linked list.
        :return: None
        """
        if self._start is None:
            raise IndexError("delete_end: Linked list is empty.")
        elif self._start == self._end:
            self._start = None
            self._end = None
            self._length -= 1
        else:
            prev = self._start
            while prev.naslednji != self._end:
                prev = prev.naslednji
            prev.next = None
            self._end = prev
            self._length -= 1

    def __len__(self) -> int:
        """
        Length of linked list returns the number of elements.
        :return: int
        """
        return self._length

    def __str__(self) -> str:
        """
        String representation of object
        :return: str
        """
        _str = ""
        knot = self._start
        while knot is not None:
            _str += "{} -> ".format(repr(knot.podatek))
            knot = knot.next
        return _str + '•'

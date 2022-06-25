from datetime import datetime as d


class DoublyLinkedList:
    class Node:
        def __init__(self, value, prev=None, next=None) -> None:
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self) -> None:
        self.head = DoublyLinkedList.Node(None)
        self.head.next = DoublyLinkedList.Node(None, self.head)
        self.tail = self.head.next
        self.size = 0

    def add_current(self, value, current) -> bool:
        """
        Helper method

        O(1) operation

        Arguments:
            @param value - the value to insert

            @param current - the node to insert the value in front of

        @returns bool - True on success
        """
        if current.next == None:
            current.next = DoublyLinkedList.Node(value, current)
        else:
            current.next = DoublyLinkedList.Node(value, current, current.next)
            if current.next.next:
                current.next.next.prev = current.next
        self.size += 1
        return True

    def add_front(self, value) -> bool:
        """
        O(1) operation
        """
        return self.add_current(value, self.head)

    def add_back(self, value) -> bool:
        """
        O(1) operation
        """
        return self.add_current(value, self.tail.prev)

    def add(self, value, idx) -> bool:
        """
        O(N) operation since it has to iterate to idx
        """
        if idx > self.size:
            return False
        current = self.head
        for i in range(idx):
            current = current.next
        self.add_current(value, current)

    def set(self, value, idx) -> bool:
        """
        O(N) operation since it has to iterate to idx
        """
        if idx >= self.size:
            return False
        current = self.head.next
        for i in range(idx):
            current = current.next
        current.value = value
        return True

    def set_front(self, value) -> bool:
        """
        O(1) operation
        """
        if self.size == 0:
            return False
        self.head.next.value = value
        return True

    def set_back(self, value) -> bool:
        """
        O(1) operation
        """
        if self.size == 0:
            return False
        self.tail.prev.value = value
        return True

    def remove_current(self, current) -> bool:
        """
        Helper method (O(1) operation)

        Arguments:
            @param current - the node to be removed

        @returns bool - True on success
        """
        current.prev.next = current.next
        if current.prev.next:
            current.prev.next.prev = current.prev
        self.size -= 1
        return True

    def remove_value(self, value) -> bool:
        """
        Attempts to remove the first occurrence of value from the list.

        O(N) operation since it has to iterate through the list to find the value

        @returns bool - True on success (value found and removed), False on failure to find the value
        """
        current = self.head.next

        # advance the cursor until either we've reached the end
        # of the list or we've reached the value
        while current != self.tail and current.value != value:
            current = current.next

        # found the item, time to remove
        if current != self.tail and current.value == value:
            self.remove_current(current)
            return True

        # didn't find the item
        return False

    def remove_front(self) -> bool:
        if self.size == 0:
            return True
        return self.remove_current(self.head.next)

    def remove_back(self) -> bool:
        if self.size == 0:
            return True
        return self.remove_current(self.tail.prev)

    def remove_idx(self, idx) -> bool:
        """
        O(N) operation since it has to iterate to idx
        """
        if idx >= self.size:
            return False
        current = self.head.next
        for i in range(idx):
            current = current.next
        return self.remove_current(current)

    def clear(self) -> bool:
        """
        O(1) operation
        """
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __str__(self) -> str:
        ret = "["
        current = self.head.next
        while current.next != None:
            ret += str(current.value)
            current = current.next
            if current.next != None:
                ret += ", "
        ret += "]"
        return ret

    def print_from_front(self) -> None:
        print(self)

    def print_from_back(self) -> None:
        current = self.tail.prev
        print("[", end="")
        while current.prev != None:
            print(current.value, end="")
            current = current.prev
            if current.prev != None:
                print(", ", end="")
        print("]")


my_double = DoublyLinkedList()
my_regular = []

TEST_SIZE = 100000

start = d.now()
for i in range(TEST_SIZE):
    my_regular.insert(0, i)
end = d.now()
print(f"it took {(end-start).total_seconds()} seconds to do that regularly")

start = d.now()
for i in range(TEST_SIZE):
    my_double.add_front(i)
end = d.now()
print(f"it took {(end-start).total_seconds()} seconds to do that doubly")

start = d.now()
for i in range(TEST_SIZE - 1):
    my_regular.pop(0)
end = d.now()
print(f"it took {(end-start).total_seconds()} seconds to do that regularly")

start = d.now()
for i in range(TEST_SIZE - 1):
    my_double.remove_front()
end = d.now()
print(f"it took {(end-start).total_seconds()} seconds to do that doubly")

print(my_regular)
print(my_double)

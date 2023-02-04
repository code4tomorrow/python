"""
In this problem, you will create a basic Doubly Linked List.
The goal is to be able to have nodes connected all the way
to 100. All you have to do is fill in the add_front and
add_back methods.
"""


class DoublyLinkedListNode:
    def __init__(self, value) -> None:
        self.value = value

        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.value}"


class DoublyLinkedList:
    def __init__(self) -> None:
        """
        Creates a head and tail node. For convenience,
        set the head to a node with the value `None`
        and the tail to a node with the value `None`.
        Sets head's next node as tail, and tail's previous
        node as head.
        Sets the size of the list to 0 as well.

        This way, the list will be "empty" when
        the head's next node is the tail (and the tail's
        previous node is the head). The purpose of these
        nodes is to make insertion and deletion much faster.
        They will not store any value besides `None` and can
        be thought of as placeholders for the beginning and
        end of the list
        """
        # create the nodes
        self.head = DoublyLinkedListNode(None)
        self.tail = DoublyLinkedListNode(None)

        # set head's next to tail, and tail's prev to head
        self.head.next, self.tail.prev = self.tail, self.head

        # set the size of the list to 0
        self.size = 0

    def add_front(self, value):
        """
        Adds a node with the provided value to the front
        of the Doubly Linked List. Increases size by 1 as well.

        By "front of the Doubly Linked List," we mean that it
        should be the node right after the placeholder head node.

        Ex: if you had nodes A, B, C, D, and you inserted node E,
        then you would have A, E, B, C, D. A's next node would be
        E, E's next node would be B, B's prev node would be E,
        and E's prev node would be A.
        """
        # create a node with the provided value
        new_node = DoublyLinkedListNode(value)

        # get the old second-to-front node
        old_second_to_front_node = self.head.next

        # change the orders
        old_second_to_front_node.prev, new_node.prev = new_node, self.head
        self.head.next, new_node.next = new_node, old_second_to_front_node

        # increase size by 1
        self.size += 1

    def add_back(self, value):
        """
        Adds a node with the provided value to the back
        of the Doubly Linked List. Increases size by 1 as well.

        By "back of the Doubly Linked List," we mean that it should
        be the node right before the placeholder tail node.

        Ex: if you had nodes A, B, C, D, and you inserted node E,
        then you would have A, B, C, E, D. C's next node would be
        E, E's next node would be D, D's prev node would be E,
        and E's prev node would be C.
        """
        # create a node with the provided value
        new_node = DoublyLinkedListNode(value)

        # get the old second-to-last node
        old_second_to_last_node = self.tail.prev

        # change the orders
        old_second_to_last_node.next, new_node.next = new_node, self.tail
        self.tail.prev, new_node.prev = new_node, old_second_to_last_node

        # increase size by 1
        self.size += 1

    def print_forward(self):
        """
        Iterates through and prints all the nodes.
        This should start at the head and end at the tail.
        """
        # ignore self.head since self.head is a "placeholder"
        cur_node = self.head.next

        while cur_node.next is not None:
            print(cur_node, end=", ")
            cur_node = cur_node.next
        print()

    def print_backward(self):
        """
        Iterates through and prints all the nodes.
        This should start at the tail and end at the tail
        """
        # ignore self.tail since self.tail is a "placeholder"
        cur_node = self.tail.prev

        while cur_node.prev is not None:
            print(cur_node, end=", ")
            cur_node = cur_node.prev
        print()

    def __len__(self):
        """
        Returns the length of the list
        """
        return self.size


our_doubly_linked_list = DoublyLinkedList()

# add the numbers 50-99
for i in range(50, 100):
    our_doubly_linked_list.add_back(i)

# add numbers 49 - 0
for i in range(49, -1, -1):
    our_doubly_linked_list.add_front(i)

# print our list forward (0 -> 99)
our_doubly_linked_list.print_forward()

# print our list backward (99 -> 9)
our_doubly_linked_list.print_backward()

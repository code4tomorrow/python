"""
Let's create a very basic version of a BST that only
has insertion capabilities. Your task will be to fill
in the node class and the BST class. The structure is somewhat
different from the BST that was given as an example, but
the logic is the same.
"""


class BSTNode:
    def __init__(self, key, value):
        """
        set self.key to key
        set self.value to the value
        create a left neighbor/child and a right neighbor/child, each of which
        start as None
        """

        # your code here
        pass

    def add_recursively(self, other_node):
        """
        Adds the other node to this node or this node's children.
        If other_node's key is equal to this node's key, do nothing.
        If other_node's key is less than this node's key, then:
            - if this node's left child is None, set this node's left child
            to that other node
            - if this node's left child is not None, then add this node
            recursively to the left child
        If other_node's key is greater than this node's key, then:
            - if this node's right child is None, set this node's right child
            to that other node
            - if this node's right child is not None, then add this node
            recursively to the right child
        """

        # your code here
        pass

    def get_value(self, key):
        """
        Tries to return the value of the node whose key matches `key`.
        If this node's key matches `key`, return this node's value.
        If the key is less than this node's key:
            - if left child is None, return 0
            - else, get the value recursively
        If the key is greater than this node's key:
            - if right child is None, return 0
            - else, get the value recursively
        """

        # your code here
        pass

    def __str__(self):
        """
        Creates and returns a string that looks like:
        left_child, self value, right_child
        However, if left child or right_child is None, don't add them
        to the string.
        """

        # your code here
        pass


class BST:
    def __init__(self):
        # set a root node to None

        # your code here
        pass

    def __setitem__(self, item, value):
        """
        create a new node whose key is item and whose value is value
        then, if root is None, set root to that node.
        else, add that node recursively.
        """

        # your code here
        pass

    def __getitem__(self, item):
        """
        Try to find the node with key that matches item.
        If no match is found, return 0
        """

        # your code here
        pass

    def __repr__(self):
        """
        Returns a string representation of the root
        """
        # your code here
        pass


my_bst = BST()
my_bst[50] = 30
my_bst[40] = 31
my_bst[60] = 32
my_bst[30] = 33
my_bst[70] = 34
my_bst[20] = 35
my_bst[80] = 36
my_bst[10] = 37
my_bst[90] = 38
print(my_bst)  # 37, 35, 33, 31, 10, 32, 34, 36, 38

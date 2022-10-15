"""
Let's create a very basic version of a BST that only
has addition capabilities. Your task will be to fill
in the node class and the BST class
"""


class BSTNode:
    def __init__(self, key, value):
        """
        set self.key to key
        set self.value to the value
        create a left neighbor/child and a right neighbor/child, each of which
        start as None
        """

        # set key, value
        self.key, self.value = key, value

        # set left child, right child
        self.left_child: BSTNode = None
        self.right_child: BSTNode = None

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
        if other_node.key == self.key:
            return  # do nothing

        if other_node.key < self.key:
            if self.left_child is None:
                self.left_child = other_node
            else:
                self.left_child.add_recursively(other_node)

        if other_node.key > self.key:
            if self.right_child is None:
                self.right_child = other_node
            else:
                self.right_child.add_recursively(other_node)

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
        if self.key == key:
            return self.value

        if key < self.key:
            if self.left_child is None:
                return 0
            else:
                return self.left_child.get_value(key)

        if key > self.key:
            if self.right_child is None:
                return 0
            else:
                return self.right_child.get_value(key)

    def __str__(self):
        """
        Creates and returns a string that looks like:
        left_child, self value, right_child
        However, if left child or right_child is None, don't add them
        to the string.
        """
        ret = ""

        # add left child to the string if it isn't None
        if self.left_child is not None:
            ret += str(self.left_child) + ", "

        # add self.value to the string
        ret += str(self.value)

        # add right child to the string if it isn't None
        if self.right_child is not None:
            ret += ", " + str(self.right_child)

        return ret


class BST:
    def __init__(self):
        # set a root node to None
        self.root = None

    def __setitem__(self, item, value):
        """
        create a new node whose key is item and whose value is value
        then, if root is None, set root to that node.
        else, add that node recursively.
        """
        # create the new node
        new_node = BSTNode(item, value)

        # either add it recursively or set it as the root
        if self.root is None:
            self.root = new_node
        else:
            self.root.add_recursively(new_node)

    def __getitem__(self, item):
        """
        Try to find the node with key that matches item.
        If root is None or no match is found return 0
        """
        if self.root is None:
            return 0
        return self.root.get_value(item)

    def __repr__(self):
        """
        Returns a string representation of the root
        """
        return str(self.root)


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
print(my_bst)

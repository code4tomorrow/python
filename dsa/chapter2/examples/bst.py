class Node:
    def __init__(self, key, value) -> None:
        # set key/value
        self.key = key
        self.value = value

        # set children to None
        self.left: Node = None
        self.right: Node = None

    def __str__(self) -> str:
        return str(self.key) + ": " + str(self.value)

    def __repr__(self) -> str:
        return str(self)


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def search(self, key):
        """
        Searches the binary tree for a node with the given key.
        Takes advantage of the fact that, in a binary tree,
        keys with lesser values go on the left and keys with greater
        values go on the right
        """
        current = self.root
        while current is not None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        raise Exception("KEY NOT FOUND")

    def get_height(self):
        """
        Gets the height of the binary tree.
        """
        if self.root is None:
            return 0

        height = 0
        next = [self.root]
        while len(next) != 0:
            temp_next = []
            height += 1
            for node in next:
                if node.left is not None:
                    temp_next.append(node.left)
                if node.right is not None:
                    temp_next.append(node.right)
            next = temp_next
        return height

    def insert_node(self, node: Node) -> None:
        """
        Tries to insert a node into the tree.
        If a node with the same key is already found,
        sets the value of that node to the value of
        the provided node
        """
        # case where root is None
        if self.root is None:
            self.root = node
            return

        # go through the nodes
        current = self.root
        while current is not None:
            if node.key == current.key:
                current.value = node.value
                return
            elif node.key < current.key:
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right

    def remove_node(self, parent, right_or_left="right"):
        """
        Helper method to remove a node.
        Notice how we have to set `parent.xxx` to something.
        This is because, in order to remove a node from a binary
        tree, what you are really doing is getting rid of all
        references to that node. So, we make sure to change
        the value stored in `parent.xxx` to a different node
        (or `None`) so that we remove the node we're trying to get rid of
        """
        if right_or_left == "right":
            node = parent.right
        else:
            node = parent.left

        if node.right is not None:
            temp = node.left
            if right_or_left == "right":
                parent.right = node.right
            else:
                parent.left = node.right

            if temp is not None:
                self.insert_node(temp)
        elif node.left is not None:
            temp = node.right
            if right_or_left == "right":
                parent.right = node.left
            else:
                parent.left = node.left
            if temp is not None:
                self.insert_node(temp)
        else:
            if right_or_left == "right":
                parent.right = None
            else:
                parent.left = None

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.insert_node(Node(key, value))

    def __delitem__(self, key):
        """
        Deletes an entry from the binary tree
        """
        # case where key to delete is the root
        if self.root is not None and self.root.key == key:
            if self.root.right is not None:
                temp = self.root.left
                self.root = self.root.right
                if temp is not None:
                    self.insert_node(temp)
            elif self.root.left is not None:
                temp = self.root.right
                self.root = self.root.left
                if temp is not None:
                    self.insert_node(temp)
            else:
                self.root = None

        # regular cases
        current = self.root
        while current is not None:
            if current.left is not None and current.left.key == key:
                self.remove_node(current, "left")
                break
            if current.right is not None and current.right.key == key:
                self.remove_node(current, "right")
                break

            if key < current.key:
                current = current.left
            if key > current.key:
                current = current.right

    def print_structure(self) -> None:
        """
        Prints out what the binary tree looks like
        """
        if self.root is None:
            print("{}")
            return

        height = self.get_height()
        spacing = 6
        total_width = spacing * (2**height)

        # print top divider
        print("-" * total_width)

        current_generation = [self.root]
        next_generation = []
        for i in range(1, height + 1):
            margin_between = int(
                (total_width - spacing * (2 ** (i - 1))) / ((2 ** (i - 1)) + 1)
            )
            for node in current_generation:
                print(" " * margin_between, end="")
                if node is None:
                    print(" " * spacing, end="")
                    next_generation.extend([None] * 2)
                else:
                    print(node, end="")
                    next_generation.extend([node.left, node.right])
            # print a newline
            print()

            current_generation = next_generation
            next_generation = []

        # print bottom divider
        print("-" * total_width)


myBinaryTree = BinaryTree()
myBinaryTree[33] = 22
myBinaryTree[22] = 11
myBinaryTree[44] = 33
myBinaryTree[55] = 22
del myBinaryTree[33]

# to see how it internally arranges data
myBinaryTree.print_structure()

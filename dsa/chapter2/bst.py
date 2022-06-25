class BinaryTree:
    class Node:
        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def __str__(self) -> str:
            ret = ""
            if self.left != None:
                ret += str(self.left)
            ret += self.plain_str() + "\n"
            if self.right != None:
                ret += str(self.right)
            return ret

        def height(self) -> int:
            if self.left == None and self.right == None:
                return 1
            if self.left != None and self.right == None:
                return 1 + self.left.height()
            if self.right != None and self.left == None:
                return 1 + self.right.height()
            return 1 + max(self.left.height(), self.right.height())

        def plain_str(self) -> str:
            return str(self.key) + ": " + str(self.value)

    def __init__(self, default_val=None) -> None:
        self.root = None
        self.default_val = default_val

    def recursive_contains_key(self, key, current) -> bool:
        if current == None:
            return False

        if current.key == key:
            return True

        if key < current.key:
            return self.recursive_contains_key(key, current.left)
        return self.recursive_contains_key(key, current.right)

    def contains_key(self, key) -> bool:
        return self.recursive_contains_key(key, self.root)

    def recursive_add(self, key, value, current):
        if current.key == key:
            current.value = value
            return True
        if key < current.key:
            if current.left != None:
                return self.recursive_add(key, value, current.left)
            current.left = BinaryTree.Node(key, value)
            return True

        if current.right != None:
            return self.recursive_add(key, value, current.right)
        current.right = BinaryTree.Node(key, value)
        return True

    def add(self, key, value) -> bool:
        if self.root == None:
            self.root = BinaryTree.Node(key, value)
            return True
        return self.recursive_add(key, value, self.root)

    def recursive_get(self, key, current):
        if current == None:
            raise Exception("KEY NOT FOUND")
        if current.key == key:
            return current.value
        if key < current.key:
            return self.recursive_get(key, current.left)
        return self.recursive_get(key, current.right)

    def get(self, key):
        return self.recursive_get(key, self.root)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __str__(self) -> str:
        ret = "{\n"
        if self.root != None:
            ret += str(self.root)
        ret += "}"
        return ret

    def __repr__(self) -> str:
        return str(self)

    def print_structure(self) -> None:
        if self.root == None:
            print("{}")
            return

        height = self.root.height()
        spacing = 6
        total_width = spacing * (2 ** height)
        print("total width is", total_width)

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
                if node == None:
                    print(" " * spacing, end="")
                    next_generation.extend([None] * 2)
                else:
                    print(node.plain_str(), end="")
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
print(myBinaryTree)

# to see how it internally arranges data
myBinaryTree.print_structure()

"""
Nodes to 10

Fill in the node class, then create nodes so that
printing start_node will print the numbers from 0 to 10.
"""


class Node:
    def __init__(self, value):
        self.value = value

        # create a neighbors list
        # your code here

    def __repr__(self) -> str:
        # start with just the node's value
        ret = f"{self.value}, "

        # add all of the neighbors' values (recursively) to the string
        for node in self.neighbors:
            ret += f"{node}"

        return ret


start_node = Node(0)

# add code that creates nodes and adds them as neighbors so that
# start_node is connected to 1, 1 is connected to 2, 2 is connected to 3,
# 3 is connected to 4, etc. If done correctly, printing start_node will
# print 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# your code here

print(start_node)

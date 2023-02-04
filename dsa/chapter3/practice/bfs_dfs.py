"""
In this practice problem, we practice implementing
breadth first search and depth first search and see them
in action
"""


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)


def BFS(start_node: Node):
    """
    Implement a breadth-first search algorithm,
    that prints the nodes that you visit as you go.

    Remember, a breadth-first search algorithm works by
    visiting all the children in a certain depth before
    advancing to the next depth

    Note that your function will be slightly different from
    the one in the example since the nodes in this file
    have children and not neighbors
    """
    # first, initialize an empty list of all visited nodes
    # next, initialize a list of all the nodes at the current depth
    # and have it contain start_node
    # lastly, create an empty list of all the nodes at the next depth.
    # your code here

    # iterate until the the list of nodes at the current depth is empty
    # in each iteration, go through all the nodes at the current depth
    # and, if it isn't in the list of visited nodes:
    #   print it
    #   add it to visited nodes
    #   add its children to the list of nodes at the next depth
    # once done iterating through all the nodes at the current depth,
    # set the list of nodes at the current depth equal to the
    # list of nodes at the next depth
    # and set the next depth to an empty list
    # your code here


def DFS(start_node: Node, visited: list = []):
    """
    Implement a recursive depth-first search algorithm,
    that prints the nodes that you visit as you go.

    Remember, a depth-first search algorithm goes all the way
    down to the last child before working its way up and visiting
    neighbors

    Note that your function will be slightly different from
    the one in the example since the nodes in this file
    have children and not neighbors
    """
    # check if the start node is in visited
    # if it isn't, then print the node
    # add it to the list of visited,
    # and then use DFS on each of its children
    # (make sure to pass the list of visited as an argument)


if __name__ == "__main__":
    # make a graph that looks like the following
    #       / 5
    #     2 - 6 - 10
    #   /
    # 1 - 3 - 7 - 11 - 12
    #   \
    #     4 - 8
    #       \ 9
    start_node = Node(1)
    for i in range(3):
        start_node.children.append(Node(i + 2))
    start_node.children[0].children.append(Node(5))
    start_node.children[0].children.append(Node(6))
    start_node.children[0].children[1].children.append(Node(10))

    start_node.children[1].children.append(Node(7))
    start_node.children[1].children[0].children.append(Node(11))
    start_node.children[1].children[0].children[0].children.append(Node(12))

    start_node.children[2].children.append(Node(8))
    start_node.children[2].children.append(Node(9))

    print("with BFS")
    BFS(start_node)  # 1 2 3 4 5 6 7 8 9 10 11 12
    print()

    print("with DFS")
    DFS(start_node)  # 1 2 5 6 10 3 7 11 12 4 8 9
    print()

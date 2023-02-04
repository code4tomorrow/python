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
    but print the nodes that you visit as you go.

    Remember, a breadth-first search algorithm works by
    visiting all the children in a certain depth before
    advancing to the next depth

    Note that your function will be slightly different from
    the one in the example since the nodes in this file
    have children and not neighbors
    """

    # initialize our lists
    visited_nodes = []
    current_depth_nodes = [start_node]
    next_depth_nodes = []

    # iterate until there are no nodes at the current depth
    while len(current_depth_nodes) != 0:
        for node in current_depth_nodes:
            if node not in visited_nodes:
                print(node, end=" ")

                # add the node to visited
                # and add its children to the list of nodes at the next depth
                visited_nodes.append(node)
                next_depth_nodes.extend(node.children)

        # "go to the next depth level" by setting
        # current_depth_nodes = next_depth_nodes
        current_depth_nodes = next_depth_nodes
        next_depth_nodes = []


def DFS(start_node: Node, visited: list = []):
    if start_node not in visited:
        print(start_node, end=" ")

        visited.append(start_node)
        for node in start_node.children:
            DFS(node, visited)


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

# simple graph
my_graph = {
    "A": {"B", "C", "E"},
    "B": {"A", "D"},
    "C": {"A"},
    "D": {"B", "E"},
    "E": {"D", "A"},
}


# graph data structure
class Node:
    def __init__(self, val: str, neighbors: list = None):
        self.val = val
        if neighbors:
            self.neighbors = neighbors
        else:
            self.neighbors = set()

    def addNeighbor(self, n):
        self.neighbors.add(n)


class Graph:
    def __init__(self, connections: list = None):
        self.nodes = {}
        if connections:
            self.parse(connections)

    def createNode(self, values: list):
        for value in values:
            self.nodes[value] = Node(value)

    def createEdge(self, n1: str, n2: str):
        self.nodes[n1].addNeighbor(self.nodes[n2])
        self.nodes[n2].addNeighbor(self.nodes[n1])

    def parse(self, connections: list):
        for connection in connections:
            if connection[0] not in self.nodes:
                self.createNode([connection[0]])
            if connection[1] not in self.nodes:
                self.createNode([connection[1]])

            self.createEdge(connection[0], connection[1])

    def __repr__(self):
        s = "{\n"
        for value in self.nodes:
            node = self.nodes[value]
            s += f"\t{value}: {[n.val for n in node.neighbors]}\n"
        s += "}"
        return s


# Takes in a list of tuples representing connections
my_graph = Graph(
    [
        ("A", "B"),
        ("B", "E"),
        ("E", "D"),
        ("D", "F"),
        ("D", "A"),
        ("A", "C"),
        ("C", "B"),
    ]
)
print(my_graph)

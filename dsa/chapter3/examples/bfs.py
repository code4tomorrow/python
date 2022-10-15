from queue import Queue


def BFS(start_node):
    visited = set(start_node)
    current_depth_nodes = Queue()
    current_depth_nodes.put(start_node)

    while len(current_depth_nodes) != 0:  # this depth is not empty
        # returns and deletes the first element
        current_node = current_depth_nodes.get()

        # add each neighbor to this depth
        for neighbor in current_node.neighbors:
            if neighbor not in visited:
                # adds element to end
                visited.add(neighbor)
                # adds element to end
                current_depth_nodes.put(neighbor)

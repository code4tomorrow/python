def recursive_dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            recursive_dfs(visited, graph, neighbour)


def iterative_dfs(graph, start):
    stack, path = [start], []

    while stack:
        node = stack.pop()
        if node in path:
            continue
        path.append(node)
        for neighbor in graph[node]:
            stack.append(neighbor)

    return path

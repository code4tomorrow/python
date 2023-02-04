from queue import PriorityQueue


def heuristic(cell, end):
    # assuming (100, 100) is end
    x1, y1 = cell
    x2, y2 = end
    return abs(x2 - x1) + abs(y2 - y1)


def reconstruct(path, end):
    final = []
    curr = end
    while curr in path:
        final.append(curr)
        curr = path[curr]

    return reversed(final)


def get_neighbors(cell, start=(0, 0), end=(100, 100)):
    def between(a, b, c):
        return (b <= a and a <= c) or (b >= a and a >= c)

    x1, y1 = cell
    return [
        (x + x1, y + y1)
        for x in range(-1, 2)
        for y in range(-1, 2)
        if (
            between(x + x1, start[0], end[0])
            and between(y + y1, start[1], end[1])
        )
    ]


def a_star(end: tuple = (100, 100), start: tuple = (0, 0)):
    count = 0
    open = PriorityQueue()
    open.put((0, count, start))
    path = {}
    g_score = {
        (x, y): float("inf")
        for x in range(end[0] + 1)
        for y in range(end[1] + 1)
    }
    g_score[start] = 0

    f_score = {
        (x, y): float("inf") for x in range(end[0]) for y in range(end[1])
    }
    f_score[0] = heuristic(start, end)

    while not open.empty():
        curr = open.get()[2]

        temp_g = g_score[curr] + 1
        for n in get_neighbors(curr, start, end):
            if n == end:
                path[n] = curr
                return reconstruct(path, end)
            if temp_g < g_score[n]:
                path[n] = curr
                g_score[n] = temp_g
                f_score[n] = temp_g + heuristic(n, end)
                if not any(n == item[2] for item in open.queue):
                    count += 1
                    open.put((f_score[n], count, n))

    # path not found
    return None


path = [coord for coord in a_star((50, 10))]
path.insert(0, (0, 0))

for y in range(0, 11):
    lst = []
    for x in range(0, 51):
        if (x, y) not in path:
            lst.append("x")
        else:
            lst.append("o")
    print(lst)

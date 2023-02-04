"""
A Star Practice

In this practice problem, you get to fill in some a_star code
as well as see the effects of using different heuristics on
a_star's execution time.

Heuristics and helper functions are given. Your job is to fill
in sections of the A* algorithm where it says 'your code here'
"""

from queue import PriorityQueue
import math
import random


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def get_neighbors(self, start, end):
        """
        This function returns a list of neighboring points
        using the fact that neighboring points will be the
        following (p = neighboring, c = current)

        ```
        p p p
        p c p
        p p p
        ```
        """

        def between(a, b, c):
            return (b <= a and a <= c) or (b >= a and a >= c)

        return [
            Point(x + self.x, y + self.y)
            for x in range(-1, 2)
            for y in range(-1, 2)
            if (
                between(x + self.x, start.x, end.x)
                and between(y + self.y, start.y, end.y)
            )
        ]

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return str(self)


def adding_heuristic(cur: Point, end: Point):
    """
    this heuristic returns a value
    that looks like the following:
    abs(x-x1) + abs(y-y1).
    """
    return abs(cur.x - end.x) + abs(cur.y - end.y)


def triangle_heuristic(cur: Point, end: Point):
    """
    this heuristic will return a value
    based off the pythagorean theorem
    that looks like the following
    sqrt((x-x1)^2 + (y-y1)^2)
    """
    return math.sqrt((cur.x - end.x) ** 2 + (cur.y - end.y) ** 2)


def bad_heuristic(cur: Point, end: Point):
    """
    This heuristic will return a value
    that is the opposite of the distance,
    meaning that the closer cur is to end,
    the worse (higher) score this will give it
    """
    return -(abs(cur.x - end.x) + abs(cur.y - end.y))


def random_heuristic(cur: Point, end: Point):
    """
    Returns a totally random number.
    """
    return random.randint(cur.x, end.x) + random.randint(cur.y, end.y)


def reconstruct_path(path: dict, start, end):
    backwards_path = []
    curr = end  # we know that we start at the end
    while curr in path:
        # add the current node to the backwards_path
        backwards_path.append(curr)

        # since path is a dictionary of node : how to get there,
        # we get the previous node in the path by doing path[curr]
        curr = path[curr]

    # this will be the first item after we reverse the list
    backwards_path.append(start)

    return reversed(backwards_path)


def a_star(start: Point, end: Point, heuristic):
    # min_x, max_x = min(start.x, end.x), max(start.x, end.x)  # uncomment this
    # min_y, max_y = min(start.y, end.y), max(start.y, end.y)  # uncomment this
    """
    initialize f_scores (final scores) to infinity for every
    point between the [min_x, min_y] and [max_x, max_y]

    initialize g_scores (distance to get there) to infinity for every
    point between [min_x, min_y] and [max_x, max_y]

    Since it takes 0 steps to get to the start, initialize that g score to 0
    """
    # your code here

    # initialize our unexplored queue and add
    # insert the start node.
    # format for inserting nodes: (f_score, count, node)
    count = 0
    unexplored = PriorityQueue()
    unexplored.put((0, count, start))

    # this is a dictionary that stores entries in the format
    # node: how to get there
    # this means that path[(1, 1)] might equal (0, 0)
    # since maybe the path goes from (0, 0) to (1, 1)
    # we use this variable to help us reconstruct the path that
    # a star found
    path = {}

    # allows us to see how many executions it really took
    num_executions = 0

    while not unexplored.empty():
        current: Point = unexplored.get()[2]  # just get the Point

        # it takes 1 more step to get to any neighbor, so their g_scores will
        # be one more than the current g score
        for node in current.get_neighbors(start, end):
            if node == end:
                # the way to get to the end is from the current node
                path[node] = current
                print(f"finished after {num_executions} executions")
                return reconstruct_path(path, start, end)
            else:
                """
                if either we haven't explored this node yet
                (meaning g_scores[node] = infinity) or this
                is a shorter path to get to this node
                (g_score[current] + 1 < g_scores[node]), then:

                * update our path
                * update our f and g scores:
                    * remember, f score = g score + heuristic
                * if it wasn't already in unexplored:
                    * update our count
                    * add the unexplored node w/ its score and count to
                      unexplored
                """
                # your code here

            num_executions += 1
    print(f"no solution found after {num_executions} executions")
    return None  # no path found


# you can try changing the heuristic and seeing how that affects the path taken
# as well as the number of executions it took
path = a_star(Point(0, 0), Point(10, 15), adding_heuristic)
path_len = 0
for i in path:
    print(i)
    path_len += 1
print(f"path length was {path_len}")

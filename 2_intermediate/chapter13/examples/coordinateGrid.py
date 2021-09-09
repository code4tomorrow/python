class coordinateGrid:
    def __init__(
        self,
        x_start: int = 0,
        x_end: int = 10,
        y_start: int = 0,
        y_end: int = 10,
    ):
        """
        Creates a list of coordinates similar to a coordinate grid.
        Each item in self.coordinates is a list representing one row in a
        coordinate grid.
        each item within that row is a point (tuple) of x, y
        ex: coordinateGrid(0, 1, -1, 1)'s coordinates would be
            [
                [(0, 1), (1, 1)],
                [(0, 0), (1, 0)],
                [(0, -1), (1, -1)]
            ]
        Arguments:
            x_start, x_end, y_start, and y_end are all inclusive
        """
        self.coordinates = [
            [(x, y) for x in range(x_start, x_end + 1)]
            for y in range(y_end, y_start - 1, -1)
        ]

    def __contains__(self, item: tuple) -> bool:
        """
        Checks to see if the provided tuple (or list)
        of length 2 (the tuple/list represents a point of x,y)
        is in self.coordinates.
        """
        return True in [item in row for row in self.coordinates]

    def __len__(self) -> bool:
        """
        In this case, we're saying that the length of the coordinateGrid
        is its area. Thus, we do height * width
        height = len(self.coordinates) and
        width = len(self.coordinates[0]) (or any row's length)
        """
        return len(self.coordinates) * len(self.coordinates[0])


grid1 = coordinateGrid(-1, 1, -1, 1)
grid2 = coordinateGrid(-10, 10, -10, 10)
point1 = (10, 10)
print(point1 in grid1)
print(point1 in grid2)
print(len(grid1))
print(len(grid2))

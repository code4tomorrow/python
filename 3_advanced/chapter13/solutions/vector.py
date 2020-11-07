"""
Define a Vector class so that the multiply operation is with
another Vector instead. The multiply operation should be the
inner or dot product of the two vectors. That means that each
element in the vector should be multiplied with its
corresponding element in the other vector, and then summed.
A scalar (regular number) should be returned.
"""

# write your code below


class Vector:
    def __init__(self, vals):
        self.vals = vals
        self.length = len(self.vals)
        self.scalar = 0

    def __mul__(self, vec):
        assert type(vec) == Vector
        a = 0
        if self.length >= vec.length:
            for i in range(vec.length):
                self.scalar += self.vals[i] * vec.vals[i]
            while a + vec.length < self.length:
                self.scalar += self.vals[i]
                a += 1
        if self.length < vec.length:
            for i in range(self.length):
                self.scalar += self.vals[i] * vec.vals[i]
            while (a + self.length) < vec.length:
                self.scalar += self.vals[i]
                a += 1
        return self.scalar


vector1 = Vector([2, 3, 2])
vector2 = Vector([3, 4, 5])
print(vector1 * vector2)  # should give 28

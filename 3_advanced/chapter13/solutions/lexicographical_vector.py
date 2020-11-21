"""
Reimplement the __lt__ and __gt__  in the given Vector
class(the one in this section) so that we are comparing
the vector's contents based on lexicographical ordering.
Think of lexicographical ordering as how you arrange words
in a dictionary. For instance, by lexicographical ordering,
'a' < 'ab', 'ab' < 'ad', 'bcd' > 'a'. It works analogously
for numbers, but instead, each character has been substituted
by a number.
"""

# write your code below


class Vector:
    def __init__(self, vals):
        self.vals = vals
        self.length = len(self.vals)
        self.scalar = 0

    def __mul__(self, vec):
        ...  # see above example

    def morecheck(self, vec, shorter):
        for i in range(shorter.length):
            if self.vals[i] > vec.vals[i]:
                return True
            if self.vals[i] < vec.vals[i]:
                return False

    def __gt__(self, vec):
        assert type(vec) == Vector
        if self.length > vec.length:
            a = self.morecheck(vec, vec)
            if a is not None:
                return a
            return True  # if all other values ==, self = longer/greater
        if self.length < vec.length:
            a = self.morecheck(vec, self)
            if a is not None:
                return a
            return False  # if all other values ==, self = shorter/smaller
        if self.length == vec.length:
            a = self.morecheck(vec, self)
            if a is not None:
                return a
            return False  # if all other values ==, self = equal/not greater

    def lesscheck(self, vec, shorter):
        for i in range(shorter.length):
            if self.vals[i] < vec.vals[i]:
                return True
            if self.vals[i] > vec.vals[i]:
                return False

    def __lt__(self, vec):
        assert type(vec) == Vector
        if self.length > vec.length:
            a = self.lesscheck(vec, vec)
            if a is not None:
                return a
            return False  # if all other values ==, self = longer/greater
        if self.length < vec.length:
            a = self.lesscheck(vec, self)
            if a is not None:
                return a
            return True  # if all other values ==, self = shorter/smaller
        if self.length == vec.length:
            a = self.lesscheck(vec, self)
            if a is not None:
                return a
            return False  # if all other values ==, self = equal/not less

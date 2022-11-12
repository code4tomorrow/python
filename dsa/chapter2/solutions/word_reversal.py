"""
Ever wanted to reverse a word a harder way?
Well, look no further than this problem that puts your
knowledge of Stacks to the test in order to solve a problem
that is already solveable by python builtins!

Your job is to reverse a string by using a stack,
adding every letter in the string (starting from the beginning of the string)
into the stack, and then popping every letter from the stack.
If done correctly, this will result in a reversed version of the string.

Starter code is given.
"""


class Stack:
    def __init__(self) -> None:
        """
        Initializes the stack. The back of the list will be
        the top of the stack (so self.items[-1] is the first item
        in the stack)
        """
        self.items = []

    def push(self, letter: str) -> None:
        """
        Adds the letter to the stack. The letter should end up
        on the *top* of the stack (the back of the list)
        """
        self.items.append(letter)

    def pop(self) -> str:
        """
        Removes the top letter from the stack. Returns this letter.
        """
        return self.items.pop()

    def __len__(self) -> int:
        return len(self.items)


def reverse_word(word: str) -> str:
    letter_stack = Stack()

    # push every letter in the word (starting from the beginning of the word)
    # into the stack
    for letter in word:
        letter_stack.push(letter)

    reversed_word = ""
    # pop every letter from the stack and add it to our reversed word
    for i in range(len(letter_stack)):
        reversed_word += letter_stack.pop()

    return reversed_word


# test code
print(reverse_word("boj doog"))
print(reverse_word("racecar"))
print(reverse_word("a man a plan a canal panama"))
print(reverse_word("read kool"))

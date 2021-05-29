# The return statement "hands back" a value
# to where the function itself was called


def average(numbers):
    # returns the average of a given list
    return sum(numbers) / len(numbers)


numbers = [1, 2, 3]

# assigns average of "numbers" to "avg" and prints it
avg = average(numbers)
print(avg)

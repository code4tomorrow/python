# Create a program that finds whether a list contains duplicates
# should return True or False
# use sets in your code


def dup_detector(item):
    theset = set(item)
    if len(theset) < len(item):
        return True
    else:
        return False


print(dup_detector([5, 4, 3, 2, 2]))  # should print True

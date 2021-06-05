# notice how there is no base
# case, meaning no way out


def recurse(i):
    i = i + 1
    print(i)
    recurse(i)


recurse(0)  # this will result in the following message:
# RecursionError: maximum recursion depth exceeded while
# calling a Python object

# RecursionError happens when you exceed your maximum
# recursion limit. By default, it is set to 1000
# you can check the maximum recursion depth by doing
# import sys
# sys.getrecursionlimit()
# you can change the maximum recursion depth by doing
# import sys
# sys.setrecursionlimit()
# However, this can be dangerous, so only do it if you
# know what you're doing.

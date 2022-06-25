def function():

    # recursive call
    function()


# recursive function
def offset(x):
    return x + 1


for number in range(10):
    print(offset(number))


def recursion(x):
    if x == 0:
        return 1
    else:
        # tail recursion happens at the return statement
        return x + recursion(x - 1)


print(recursion(6))

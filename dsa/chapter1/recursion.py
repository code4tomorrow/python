def function():

    # recursive call, however this will run forever
    function()


def offset(x):
    return x + 1


for number in range(10):
    print(offset(number))


# recursive function
def recursion(x):
    if x == 0:
        return 1
    else:
        # tail recursion happens at the return statement
        return x + recursion(x - 1)


print(recursion(6))

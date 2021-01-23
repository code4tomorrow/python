# Write a function that takes two parameters and tries to divide
# parameter 1 by parameter 2 to get a result and print that result.
# However, if something goes wrong, have an except print a message
# saying "something went wrong" (optional: have specific messages
# for different errors). Finally, it should, no matter what, print
# "Goodbye World" when it is done.


def finally_use(num1, num2):
    try:
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by Zero")
    except TypeError:
        print("Invalid type for division")
    finally:
        print("Goodbye World")


finally_use(4, 0)
finally_use(5, "hi")
finally_use(8, 4)

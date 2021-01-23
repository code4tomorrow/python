# Write a function that accesses a global list. It should try to
# take the user’s input for how many times to repeat its process.
# Its process should be: 1. ask the user for a value (any type)
# 2. Append that value to the list. Once that is done, ask the user
# to press q to quit or to input a number to access that index of the
# list. There should be a different error message depending on the type
# of error raised. Whether or not there are errors, when the user is done
# (or there is an error), it should print the list and ask the user
# whether they would like to continue. If this input is 'y', call the
# function again.

globlist = []


def list_practice():
    global globlist
    try:
        times = int(input("How many times would you like to do this? "))
        for i in range(times):
            globlist.append(input("What to append? "))
        myinput = input(
            "press q to quit; input a number to access " +
            "that value in the list"
        )
        while myinput != "q":
            print(globlist[int(myinput)])
            myinput = input(
                "press q to quit, input a number to access " +
                "that value of the list"
            )
    except ValueError:
        print("That's not a number")
    except IndexError:
        print("That's out of range")
    finally:
        print("This is the list you ended up with: ", globlist)
        cont = input("try again? y/n ")
        if cont == "y":
            list_practice()


list_practice()

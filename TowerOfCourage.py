# Story + Directions: This Summer, an amusement
# park introduced a new ride call Tower of Courage.
# In this ride, each car can hold up to 10 people. However,
# for safety, the weight of the riders has to be checked and
# distributed evenly. Help the amusement park  by writing a function
# that asks each of the rider's weights. The function should return
# this list and then print out the list, sum, and average weights.


def weight():
    # introduce the list for all riders
    lstRider = []

    # loop throught the 10 people ask the weight and add to list
    for i in range(1, 11):
        weight = input(f"Enter rider {str(i)}'s weight (or q to quit): ")

        if weight == "q":
            break
        else:
            lstRider.append(int(weight))

    return lstRider


# set the function equal to the variable
lstRider = weight()

# to calculate the sum of weights
total = 0

for i in range(0, 10):
    total += lstRider[i]

# print the three outputs that are required
print("The list of all the weights:")
print(lstRider)
print(f"The sum of all the weights is {str(total)}.")
print(f"The average weight of the passengers is {str(total/10)}.")

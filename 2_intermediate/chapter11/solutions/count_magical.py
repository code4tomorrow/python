# Write a function called count_magical
# that returns the number of even numbers
# in a given list. In the function,
# if the number of evens is greater than
# half of the length of the list, print "Magical"
# Else, print "Not Magical"

def count_magical(my_list):
    number_of_evens = 0
    for n in my_list:
        if n % 2 == 0:
            number_of_evens += 1

    if number_of_evens > len(my_list) / 2:
        print("Magical")
    else:
        print("Not Magical")

    return number_of_evens

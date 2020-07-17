# Write a function called count_magical
# that returns the number of even numbers
# in a given list. In the function,
# if the number of evens is greater than
# half of the length of the list, print "Magical"
# Else, print "Not Magical"
#
# Write a function called main which tests
# the count_magical function on at least
# 3 different lists of integers. Use the main
# function to test count_magical by calling main().


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


def main():
    list_1 = [1, 2, 3, 4, 5, 6]  # not magical, 3 evens
    list_2 = [0, 35, 1, 35, 2, 4]  # not magical, 3 evens
    list_3 = [10, 20, 12, 3, -9]  # magical, 3 evens

    print("Number of evens in list 1:", count_magical(list_1))
    print("Number of evens in list 2:", count_magical(list_2))
    print("Number of evens in list 3:", count_magical(list_3))


main()

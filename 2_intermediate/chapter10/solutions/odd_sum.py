# Odd Sum
# Given a 2D list, find the sum of all elements at odd indexes for all
# the lists at odd indexes. Print this sum times the sum of all
# first element of all the 1D lists in the 2D list.
#
# Ex:[[1,2,3,6],[2,41,2,1]]should have print 42 after the program runs.
#
# Write the code below.

two_d_list = [[1,2,3,5,2],[2,3,1,4],[2,3,1,2,21],[21,3,1,41]]
#two_d_list should print 51 after the program runs.

odd_sum = 0
for outer_idx in range(1,len(two_d_list),2):
    for inner_idx in range(1, len(two_d_list[outer_idx]),2):
        odd_sum += two_d_list[outer_idx][inner_idx]

first_sum = 0
for inner_list in range(len(two_d_list)):
    first_sum += two_d_list[inner_list][0]

print(odd_sum* first_sum )


        

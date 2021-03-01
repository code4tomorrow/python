"""
The following code is not meant to be run because
there's no input. Instead, analyze it's running time
in terms of Big-O. The first two lines are already
analyzed for you. Do the same for all the other lines.
At the end, put the total running time of code.
The input of the problem is ex_2d_list, and assume
it has n numbers. This problem assumes you have the
knowledge of 2D Lists.


ex_2d_list = [[?,?,?],[?,?]...]#Input,O(1)
list_sum = 0#O(1)
for ex_1d_list in ex_2d_list:#This line and next line combined = O(n)
    for element in ex_1d_list:
        list_sum += element#O(1)
print(list_sum)#O(1)
#Total running time = O(n)
#
#Explanation: We are finding the running time in terms of the input.
#The whole 2d list has n elements so the double for loop will loop
#n times in total.
"""

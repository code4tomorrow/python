"""
The following code is not meant to be run because
there's no input. Instead, analyze it's running time
in terms of Big-O. The first two lines are already
analyzed for you. Do the same for all the other lines.
The input of the problem is ex_list, and assume it
has n elements. At the end, put the total running
time of code. Note: You will be surprised!


ex_list = [?,?,?,...]#Input,O(1)
for i in range(len(ex_list)):#O(n)
    print(i)#O(1)
    ex_list.append(i)#O(1)
for i in ex_list:#No Big-O. Runs forever.
    print(i)#O(1)
    ex_list.append(i)#O(1)	
#Total running time = There is no upper bound, so
#no Big-O.
#
#Explanation: The second for loop will keep looping
#since ex_list will keep increasing in size each time
#you loop. You may ask why doesn't the first for loop do
#the same? That is because the number of times the first
#for loop loops is set at the very start of the loop,
#whereas for the second for loop will keep looping until
#every element is checked.
"""

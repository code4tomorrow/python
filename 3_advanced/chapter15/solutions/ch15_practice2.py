"""
The following code is not meant to be run because
there's no input. Instead, analyze it's running time
in terms of Big-O. The first two lines are already
analyzed for you. Do the same for all the other lines.
The input of the problem is ex_list, and assume it has
n elements. At the end, put the total running time of
code.


ex_list = [?,?,?,...]#Input,O(1)
for i in range(2):#O(1)
    ex_list.insert(0,1)#O(n)
    ex_list.append(1)#O(1)
for number in ex_list:#O(1)
    for number in ex_list:#O(1)
        break#O(1)
    break#O(1)
#Total running time = O(n)
"""

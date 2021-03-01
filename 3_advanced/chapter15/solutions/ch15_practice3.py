"""
The following code is not meant to be run because
there's no input. Instead, analyze it's running time
in terms of Big-O. The first two lines are already
analyzed for you. Do the same for all the other lines.
The input of the problem is ex_list, and assume it
has n elements. At the end, put the total running
time of code.


ex_list = [?,?,?,...]#Input,O(1)
for i in range(len(ex_list)):#O(n)
    if i%2 == 0:#O(1)
        print(1)#O(1)
    else:#O(1)
        print(2)#O(1)
    for j in range(len(ex_list)):#O(n)
        for k in range(len(ex_list)):#O(n)
            print(j,k)#O(1)
#Total running time = O(n^3)
"""

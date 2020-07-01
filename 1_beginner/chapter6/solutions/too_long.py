"""
Too Long
Print and remove all elements in a given list with length greater than 4.
"""
the_list = ['dragon', 'cab', 'science', 'dove', 'lime', 'river', 'pop']

for x in the_list:  #iterates through every element in the_list
    if(len(x) > 4): #if length is greater than 4
        print(x)    #print it
        the_list.remove(x)

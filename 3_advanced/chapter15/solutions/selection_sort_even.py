"""
The Selection Sort code we saw sorts an array from least to greatest.
Modify this code so that the code sorts only the elements at the even
indexes, ignoring elements at odd indexes.

Selection Sort Code:

arr  = [?,?,?]#change this array to the array you want to sort
for first_idx in range(len(arr)):
    min_idx = first_idx
    for second_idx in range(first_idx+1, len(arr)):
        if arr[second_idx] < arr[min_idx]:
            min_idx = second_idx
    arr[first_idx], arr[min_idx] = arr[min_idx], arr[first_idx]

"""

#write your code below

arr  = [4,1,2,5,123,98,23]
for first_idx in range(0,len(arr),2):#range(start, stop, step)
    min_idx = first_idx
    for second_idx in range(first_idx, len(arr),2):
        if arr[second_idx] < arr[min_idx]:
            min_idx = second_idx
    arr[first_idx], arr[min_idx] = arr[min_idx], arr[first_idx] 
   
print(arr)

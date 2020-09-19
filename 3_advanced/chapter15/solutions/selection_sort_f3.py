"""
The Selection Sort code we saw sorts an array from least to greatest.
Modify this code so that the code sorts only the first three elements
of an array.

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
f3_arr = arr[:3]#this will contains the elements before the 3rd index.
remaining_arr = arr[3:]#this will be [] if original arr <= 3
for first_idx in range(len(f3_arr)):
    min_idx = first_idx
    for second_idx in range(first_idx+1, len(f3_arr)):
        if f3_arr[second_idx] < f3_arr[min_idx]:
            min_idx = second_idx
    f3_arr[first_idx], f3_arr[min_idx] = f3_arr[min_idx], f3_arr[first_idx]

print(f3_arr + remaining_arr)#adding lists will combine the lists

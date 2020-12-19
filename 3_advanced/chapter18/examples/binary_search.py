#Code for binary search

def binary_search(arr, low, high, x):
    """
    Parameters:
    1)arr is the sorted array in which we will be finding the element
    2)low is the lower bound of the interval in which we will
    be finding the element index
    3)high is the upper bound of the interval in which we will
    be finding the element index
    4)x is the element we are trying to find the index of

    Output: the index of the element x in the array arr.
    If the element x does not exist in array arr, -1 will
    be returned.
    """

    while high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:   #Base Case 1
            return mid
        elif arr[mid] < x:  #Recursive Case 1
            return binary_search(arr, mid + 1, high, x)
        else:               #Recursive Case 2
            return binary_search(arr, low, mid - 1, x)
    else:                   #Base Case 2: element not found
        return -1
    
print(binary_search([1,24,28,30,40,52], 0, 5, 28))

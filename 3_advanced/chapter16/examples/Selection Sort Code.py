arr = [1, 4, 2, 7, 7, 6]  # change this array to the array you want to sort
for first_idx in range(len(arr)):
    min_idx = first_idx
    for second_idx in range(first_idx + 1, len(arr)):
        if arr[second_idx] < arr[min_idx]:
            min_idx = second_idx
    arr[first_idx], arr[min_idx] = arr[min_idx], arr[first_idx]

print(arr)

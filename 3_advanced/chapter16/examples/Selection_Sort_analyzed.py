arr = [int, int, int]  # this is the input, so we're not analyzing it
for first_idx in range(len(arr)):  # O(n)
    min_idx = first_idx  # O(1) * O(n) = O(n)
    for second_idx in range(first_idx + 1, len(arr)):  # O(n) * O(n) = O(n^2)
        if arr[second_idx] < arr[min_idx]:  # O(1) * O(n) * O(n) = O(n^2)
            min_idx = second_idx  # O(1) * O(n) * O(n) = O(n^2)
    arr[first_idx], arr[min_idx] = (
        arr[min_idx],
        arr[first_idx],
    )  # O(1) * O(n) = O(n)

# Sum = O(n) + O(n) + O(n^2) + O(n^2) + O(n^2) + O(n)
# Sum = 3*O(n) + 3*O(n^2)
# Final Running Time = O(n^2)

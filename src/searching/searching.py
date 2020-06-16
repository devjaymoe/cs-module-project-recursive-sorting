# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0 :
        return -1
    # base case if target == mid
    mid = (end + start) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] > target:
        # check the left side
        # mid is the high point
        return binary_search(arr[:mid], target, start, mid)
    else:
        return binary_search(arr[mid:], target, mid, end)

    return -1  # not found

# arr = [1, 2, 3, 4, 5, 6, 7]
# print(binary_search(arr, 2, 0, len(arr)))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

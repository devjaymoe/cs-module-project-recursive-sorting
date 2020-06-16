# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # pointers to navigate through their arrays
    aPointer = 0
    bPointer = 0
    # Your code here
    # loop through the length of arrays
    for index in range(len(merged_arr)):
        # compare elements of the array to see which
        # since they are sorted if they ever reach the end you can merge the rest
        # of the remaining array to the end of the merged array
        # will be added to the merged array
        if aPointer == len(arrA):
            merged_arr[index] = arrB[bPointer]
            bPointer += 1
        # do the same for the bPointer
        elif bPointer == len(arrB):
            merged_arr[index] = arrA[aPointer]
            aPointer += 1
        # else block if the end of the array hasn't been reached
        else:
            # check the individual values at the start of each array
            if arrA[aPointer] > arrB[bPointer]:
                # if a is larger then b will get put onto the merged array
                # at the index of the merged array
                merged_arr[index] = arrB[bPointer]
                bPointer += 1
                # otherwise a is smaller and add that to the merged array
            else:
                merged_arr[index] = arrA[aPointer]
                # check to see if pointer is at the end of its array
                aPointer += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case is arr length of 1 or 0
    # if it is 1 then it is sorted
    if len(arr) <= 1:
        return arr
    else:
        # array split
        splitter = len(arr) // 2
        # recursively calls on both sides
        # call on the left side to divide it into sub arrays
        arr1 = merge_sort(arr[:splitter])
        # call on the right side to divide it into sub arrays
        arr2 = merge_sort(arr[splitter:])
        return merge(arr1, arr2)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

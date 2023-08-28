#merge sort 
#time complexity O(nlogn), space O(n)

def merge(arr, left, right):
    nl = len(left) # lenght of left array
    nr = len(right) #lenght of right array
    i, j, k = 0, 0, 0

    while i<nl and j<nr: 
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1     
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    #fill the rest ogf the remaining elements 
    while i < nl: #for the left of sub array
        arr[k] = left[i]
        i+=1 
        k+=1
    while j < nr:
        arr[k] = right[j]
        j += 1
        k += 1
    
def mergeSort(arr):
    #base condition to exit from recursion 
    # when there is only one element left in the array
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    left = arr[: mid]
    right = arr[mid : ]

    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)


ls = [3,8,1,90,34,2,7,4,6]
mergeSort(ls)
print(ls)
    
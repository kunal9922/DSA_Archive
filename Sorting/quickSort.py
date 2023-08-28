# Inplace algo 
# Space Complexity O(1), time O(nlogn)

def partition(arr, start, end):
    piviot = arr[end]
    pidx = start
    for i in range(start, end):
        if(arr[i] <= piviot):
            #swap
            arr[i] , arr[pidx] = arr[pidx] , arr[i]
            pidx += 1
    # swap the value with the piviot value 
    arr[end] , arr[pidx] = arr[pidx], arr[end]

    #return the partion index
    return pidx

def quickSort(arr, start, end):
    if(start >= end): # exit condition of recursion and handle invalid index senerio
        return 
    pIndex = partition(arr, start, end)
    quickSort(arr, start, pIndex-1)
    quickSort(arr, pIndex+1, end)

arr = [6,3,7,1,9,10,4,4]
quickSort(arr, 0, 7)
print(arr)



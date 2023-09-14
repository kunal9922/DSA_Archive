def bubbleSort(array: list):
    '''InPlace sorting with the time complexity O(n^2)'''
    n = len(array)
    for k in range(n-1):
        FLAG = False # Check if the it passes trough the array
        for i in range(n-k-1):
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i+1], array[i]
                FLAG = True
            
        if FLAG is False: # if we didn't do any swaps that means we have already dorted array
            break
    

myArray = [4,1,2,9,0,3,6,5]
bubbleSort(myArray)
print(myArray)

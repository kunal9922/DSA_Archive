def selectionSort(array: list):
    '''In palce sorting with the O(n^2) time complexity'''
    n = len(array)
    for i in range(n-1): # We need to do n-2 passes
        iMin = i # ith position elements form i till n-1
        for j in range(i+1, n):
            if array[j] < array[iMin]:
                iMin = j # Update the index of minimum elements from i till n-1
            
            # Swap the values
        array[i] , array[iMin] = array[iMin], array[i]

myArray = [2, 7, 4, 1, 5, 3]
selectionSort(myArray)
print(myArray)
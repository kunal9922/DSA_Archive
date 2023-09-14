def insertionSort(array: list):
    n = len(array)
    for i in range(1, n-1):
        value = array[i]
        hole = i
        while hole > 0 and array[hole - 1] > value:
            # Shift the element by one position
            array[hole] = array[hole - 1]
            hole -= 1
        
        array[hole] = value
    
histogram = [2, 1, 5, 6, 2, 3]
insertionSort(histogram)
print(histogram)
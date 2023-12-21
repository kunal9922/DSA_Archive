# Heap Sort 
import math

class Heap():
    def heapSort(self, array: []) -> list:
        self.buildMaxHeap(array)
        n = len(array)
        for i in range(len(array)-1, -1, -1):
            array[0], array[i] = array[i], array[0]
            n -= 1 
            self.heapify(array, 0)
            
    
    def buildMaxHeap(self, array):
        n = len(array)
        for i in range(math.floor(n/2)-1, -1, -1 ):#math.floor(n-1/2), -1, -1):
            self.heapify(array, i)
        
    def heapify(self, array, i):
        n = len(array)
        left = 2 * i 
        right = 2 * i + 1
        MAX = 0
        #To check the left subtree value with the parent's value
        if left <= n:
            if array[left] > array[i]:
                MAX = left
        else:
            MAX = i
            
        #To check the Right subtree value with the parent's value
        if right <= n:
            if array[right] > array[MAX]:
                MAX = right
        
        if MAX != i: # Swap array values 
            array[i], array[MAX] = array[MAX], array[i]
            self.heapify(array, MAX)
            
listOfRollNos = [4,7,2,5,1,9,10, 3]

# Before heap sorting
print(listOfRollNos)

heapObj = Heap()
heapObj.heapSort(listOfRollNos)

# After heap sorting
print(listOfRollNos)

# time complexity from top to bottom of heap is O(logN)
# Total time complexity is O(N logN)


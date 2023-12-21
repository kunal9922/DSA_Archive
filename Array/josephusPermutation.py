# Using Double Ended Queue for the best performance
from collections import deque
def solution(array: list, k: int):
    # Deck = double ended queue
    deck = deque(array) 
    permutation = []
    while deck:
        deck.rotate(1 - k)
        item = deck.popleft()
        permutation.append(item)
        
    return permutation

import time
soldiers = 7
arr = [s + 1 for s in range(soldiers)]
k = 3
start = time.perf_counter()
perm = solution(arr, k)
stop = time.perf_counter()
print(perm)
print("Time took", stop - start)

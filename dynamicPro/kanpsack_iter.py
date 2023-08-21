#knapsack problem with itreative approach
knapSize = 5
items = 3
# creating a table for memorization
memoTable = [[0] * (knapSize+1) for _ in range(items+1)]

weightOfItems = [1, 2, 3]
profits = [2, 3, 4]

def knapsack_iter():
    global memoTable, weightOfItems, profit, knapSize, items

    for i in range(0, items+1): #weights loop
        for j in range(0, knapSize+1): # knap capacity 
            #first case: no item and no weight to procced
            if i == 0 or j ==0:
                memoTable[i][j] = 0
            # skip the weight (weightOfItem > knap capacity)
            elif weightOfItems[i-1] > j:
                memoTable[i][j] = memoTable[i-1][j]
            # weightofItem <= knapCapacity
            else: 
                memoTable[i][j] = max(memoTable[i-1][j], profits[i-1] + memoTable[i-1][knapSize - weightOfItems[i-1]] )

knapsack_iter()
print(memoTable)
# knapSack problem 
# recursive approach
#memorization Timecomplexity O(knapSize. size)

knapSize = 8
items = 5
memo = [[-1] * (knapSize+1) for _ in range(items+1)]
print(memo)

def knapsack(weight: list, profit: list, knap, n):
    if knap == 0 or n == 0:
        return 0 # that mean we are run out of knap capacity or no elements to process
    #memorization of pre calculated task
    if memo[n][knap] != -1:
        return memo[n][knap]
    # skip the weight 
    if weight[n-1] > knap:
        return knapsack(weight, profit, knap, n-1)
    # include the weight
    else:
        result =  max(
            profit[n-1] + knapsack(weight, profit, knap - weight[n-1], n-1),
            knapsack(weight, profit, knap, n-1)
        )
    memo[n][knap] = result
    return result


w = [12, 5, 2, 6, 40]
p = [20, 3, 70, 9, 100]
profit = knapsack(w, p, knapSize, items)
print(profit)    
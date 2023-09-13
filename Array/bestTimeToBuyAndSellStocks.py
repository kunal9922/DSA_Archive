class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 # Left for Buy and Right for Sell
        maxProfit = 0 # No Profit till yet

        while r < len(prices):
            if prices[l] < prices[r]:
                # Found less priced stock
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r
            r += 1
        
        return maxProfit

stocksPrices = [7, 1, 5, 3, 6, 4]
find = Solution()
maxProfitGet = find.maxProfit(stocksPrices)
print(maxProfitGet)
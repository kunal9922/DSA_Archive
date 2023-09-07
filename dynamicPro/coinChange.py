class DynamicProgramming:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # Time O(amount + len(coins))
        # space O(amount)
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
    

dp = DynamicProgramming()
coins = [1, 3, 4, 5]
amount = 7

print(dp.coinChange(coins, amount))
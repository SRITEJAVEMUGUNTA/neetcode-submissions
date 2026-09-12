class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float("inf") for _ in range(amount+1)]
        arr[0] = 0

        for amt in range(amount+1):
            for c in coins:
                if amt - c >= 0:
                    arr[amt] = min(arr[amt], 1+arr[amt-c])
        print(arr)
        return arr[amount] if arr[amount] != float("inf") else -1
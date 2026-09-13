class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [0 for _ in range(amount + 1)]
        arr[0] = 1

        for c in coins:
            for amt in range(amount + 1):
                if amt-c >= 0:
                    arr[amt] += arr[amt-c]
        
        return arr[amount]


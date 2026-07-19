class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = []
        res = [0 for i in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while arr and arr[-1][0] < temp:
                _, idx = arr.pop()
                res[idx] = i - idx
            arr.append([temp,i])

        return res

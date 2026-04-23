class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append([temp, i])
                continue

            
            while stack and stack[-1][0] < temp:
                _, idx = stack.pop()
                res[idx] = i - idx

            
            stack.append([temp, i])

        return res
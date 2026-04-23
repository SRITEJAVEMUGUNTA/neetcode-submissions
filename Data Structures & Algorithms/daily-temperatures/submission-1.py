class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]

        stack = []

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append([i, temp])
                continue

            while stack and temp > stack[-1][1]:
                popped_i, _ = stack.pop()
                res[popped_i] = i - popped_i
            

            stack.append([i, temp])

        return res
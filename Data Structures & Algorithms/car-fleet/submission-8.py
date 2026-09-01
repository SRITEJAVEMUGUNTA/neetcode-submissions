class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            p = position[i]
            s = speed[i]
            t = (target - p) / s
            arr.append([p, t])
        arr.sort()
        stack = []
        for p, t in arr:
            while stack and stack[-1][1] <= t:
                stack.pop()
            stack.append([p, t])
        
        return len(stack)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []

        for i in range(len(position)):
            t = (target - position[i])/speed[i]
            time.append([position[i], t])

        
        time.sort(reverse=True)
        stack = []


        for _, t in time:
            if not stack or stack[-1] < t:
                stack.append(t)
        

        return len(stack)
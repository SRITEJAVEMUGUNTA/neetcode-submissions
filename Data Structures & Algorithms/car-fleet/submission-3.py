class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []

        for i in range(len(position)):
            pos = position[i]
            spe = speed[i]
            time.append([pos, (target-pos) / spe])

        time.sort()

        stack = []

        for pos, time in time:
            if not stack:
                stack.append(time)
                continue
            while stack and stack[-1] <= time:
                stack.pop()

            stack.append(time)
        
        return len(stack)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        for i in range(len(gas)):
            cur = gas[i] - cost[i]
            idx = (i+1) % len(gas)
            flag = True

            while idx != i:
                if cur < 0:
                    flag = False
                    break
                cur += (gas[idx] - cost[idx])
                print(cur)
                idx += 1
                idx %= len(gas)
            if flag and cur >= 0:
                return i
                

        return -1
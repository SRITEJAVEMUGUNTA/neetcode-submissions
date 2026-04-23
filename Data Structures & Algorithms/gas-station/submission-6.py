class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        net = 0
        idx = 0

        for i in range(len(gas)):

            net += (gas[i]-cost[i])

            if net < 0:
                idx = i + 1
                net = 0

        return idx
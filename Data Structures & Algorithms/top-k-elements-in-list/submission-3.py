class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)

        sol = []

        while k > 0:
            freq = 0
            key = 0
            for x in dic:
                if(dic[x] > freq):
                    freq = dic[x]
                    key = x
            k -= 1
            dic.pop(key)
            sol.append(key)
        return sol
            
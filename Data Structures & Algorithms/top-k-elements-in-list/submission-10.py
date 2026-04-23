class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)

        counts = [[] for _ in range(len(nums) + 1)]

        for num in dic:
            counts[dic[num]].append(num)

        

        res = []

        for i in range(len(nums), -1, -1):
            if not counts[i]: continue
            j = 0
            while len(res) < k and j < len(counts[i]):
                res.append(counts[i][j])
                j += 1

            if len(res) == k:
                return res

        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        count = defaultdict(list)

        for num in dic:
            count[dic[num]].append(num)

        
        res = []
        for i in range(len(nums), -1, -1):
            if not count[i]:
                continue

            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        
        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)

        arr = [[] for _ in range(len(nums))]


        for key in dic:
            arr[dic[key]-1].append(key)

        
        res = []
        idx = len(nums) - 1
        while len(res) < k:
            res.extend(arr[idx])
            idx-=1
        
        return res
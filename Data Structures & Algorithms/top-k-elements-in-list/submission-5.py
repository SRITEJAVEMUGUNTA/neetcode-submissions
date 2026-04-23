class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dic = Counter(nums)
        arr = [[] for i in range(len(nums)+1)]
        for key in dic:
            arr[dic[key]].append(key)


        count = 0
        
        for i in range(len(arr) - 1, -1, -1):
            for num in arr[i]:
                res.append(num)
                count += 1

                if count == k:
                    return res

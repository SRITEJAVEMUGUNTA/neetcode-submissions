from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        backwards = defaultdict(list)
        for key in dic:
            backwards[dic[key]].append(key)
        count = 0
        res = []
        for i in range(len(nums), -1, -1):
            if backwards[i]:
                idx = 0
                while count < k and idx < len(backwards[i]):
                    res.append(backwards[i][idx])
                    idx += 1
                    count += 1
            
            if count == k:
                break
        
        return res


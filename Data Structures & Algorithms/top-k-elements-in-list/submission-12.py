class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums))]

        dic = Counter(nums)
        print(dic)
        for num, cnt in dic.items():
            arr[cnt-1].append(num)


        res = []
        idx = len(nums) - 1
        while len(res) < k: 
            res.extend(arr[idx])
            idx -= 1

        return res
            
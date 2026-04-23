class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        solution = []

        for x in nums:
            if x in dic.keys():
                dic[x] += 1
            else:
                dic[x] = 1

        #print(dic)
    
        count = 0
        while count < k:
            frequent = 0
            key_needed = 0
            for x in dic.keys():
                if dic[x] > frequent:
                    frequent = dic[x]
                    key_needed = x
            solution.append(key_needed)
            dic.pop(key_needed)
            count += 1
        return solution
            
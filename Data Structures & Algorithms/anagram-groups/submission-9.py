class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            dic["".join(sorted(word))].append(word)
        
        
        res = []
        for key in dic:
            res.append(dic[key])
        return res
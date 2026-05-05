class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            sortedWrd = "".join(sorted(word))

            dic[sortedWrd].append(word)

        return [arr for arr in dic.values()]
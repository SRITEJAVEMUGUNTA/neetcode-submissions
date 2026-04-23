class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        seen = set()
        def helper(start, arr, total):
            if total == target:
                newArr = [str(num) for num in arr]
                string = "#".join(newArr)
                print(string)
                if string not in seen:
                    res.append(arr.copy())
                    seen.add(string)
                return
            if total > target:
                return
            

            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                helper(i+1, arr, total + candidates[i])
                arr.pop()

        helper(0,[],0)
        return res
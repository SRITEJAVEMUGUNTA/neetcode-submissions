class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(idx, arr, total):
            if total == target:
                res.append(arr.copy())
                return

            if total > target or idx >= len(candidates):
                return

            for i in range(idx, len(candidates)):

                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                if total + candidates[i] > target:
                    break
                
                arr.append(candidates[i])
                helper(i+1, arr, total + candidates[i])
                arr.pop()


        

        helper(0, [], 0)
        return res
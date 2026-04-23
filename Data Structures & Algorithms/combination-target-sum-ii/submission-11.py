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

            arr.append(candidates[idx])
            helper(idx+1, arr, total + candidates[idx])
            arr.pop()

            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx+1]:
                idx += 1
            
            helper(idx+1, arr, total)


        

        helper(0, [], 0)
        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(idx, arr, total):
            if total == target:
                res.append(arr.copy())
                return
            
            if idx >= len(candidates) or total > target:
                return

            i = idx
            while i < len(candidates):
                while i > idx and i < len(candidates) and candidates[i] == candidates[i-1]:
                    i += 1
                
                if i >= len(candidates) or total + candidates[i] > target:
                    break

                arr.append(candidates[i])
                helper(i+1, arr, total + candidates[i])
                arr.pop()

                i += 1
        

        helper(0,[],0)

        return res
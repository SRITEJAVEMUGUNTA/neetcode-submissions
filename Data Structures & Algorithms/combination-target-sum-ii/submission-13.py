class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(arr, idx, total):
            if total == target:
                res.append(arr.copy())
                return

            if idx == len(candidates): return
            if total > target: return


            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                arr.append(candidates[i])
                backtrack(arr, i+1, total + candidates[i])
                arr.pop()

        backtrack([], 0, 0)
        print(res)
        return res
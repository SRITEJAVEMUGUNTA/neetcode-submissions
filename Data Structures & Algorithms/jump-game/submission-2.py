class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(idx):
            if idx == len(nums) - 1:
                return True

            
            if nums[idx] == 0:
                return False
            
            if idx in memo:
                return memo[idx]


            distance = min(len(nums), nums[idx]+1)
            flag = False
            for i in range(1, distance):
                if dfs(idx + i):
                    print(idx)
                    print(i)
                    print('\n')
                    flag = True
                    break
                
            if flag:
                memo[idx] = True
                return True
            
            memo[idx] = False
            return False

        return dfs(0)


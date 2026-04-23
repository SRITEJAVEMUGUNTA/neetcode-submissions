class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0
        x = None
        while True:
            print(slow)
            print(fast)
            print("\n")
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                x = slow
                break

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow

            

        
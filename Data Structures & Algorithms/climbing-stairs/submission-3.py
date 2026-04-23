class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        There is 1 way to climb one step

        There is 2 ways to climb two steps

        There is 3 ways to climb three steps

        There is 5 ways to climb four steps
            1+1+1+1 = 4
            2+1+1 = 4
            1+1+2 = 4
            1+2+1 = 4
            2+2 = 4
        '''

        one = 1
        two = 1

        for x in range(n - 1):
            temp = one + two

            one = two

            two = temp
        
        return two
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort() # 0(nlogn)

        prevInterval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]

            if prevInterval[1] >= curStart:
                prevInterval = [prevInterval[0], max(curEnd, prevInterval[1])]
            else:
                res.append(prevInterval)
                prevInterval = intervals[i]

        res.append(prevInterval)

        return res

            


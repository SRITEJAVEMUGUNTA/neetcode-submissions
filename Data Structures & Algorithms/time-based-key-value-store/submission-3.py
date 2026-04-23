from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        if len(self.dic[key]) < 1:
            return ""

        if self.dic[key][0][1] > timestamp:
            return ""
        
        arr = self.dic[key]

        l, r = 0, len(arr) - 1
        closest = -1
        while l <= r:
            mid = (l+r) // 2
            val, time = arr[mid]

            if time == timestamp:
                return val
            elif timestamp > time:
                closest = mid
                l = mid + 1
            else:
                r = mid - 1

        return arr[closest][0]


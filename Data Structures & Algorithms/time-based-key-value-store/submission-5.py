from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])
        print(self.dic[key])

    def get(self, key: str, timestamp: int) -> str:
        if not self.dic[key]: return ""


        arr = self.dic[key]


        l, r = 0, len(arr)-1
        res = ""
        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                r = mid - 1
            else:
                res = arr[mid][1]
                l = mid + 1
            
        return res

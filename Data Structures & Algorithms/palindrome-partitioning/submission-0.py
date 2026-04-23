class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(arr,idx, start):
            if idx == len(s):
                print(arr)
                flag = True
                count = 0
                for string in arr:
                    count += len(string)
                    if string != string[::-1]:
                        flag = False
                        break
                print(count)
                if flag and count == len(s):
                    res.append(arr.copy())
                
                return
            oldStart = start
            # include the current letter in the array
            arr.append(s[start:idx+1])
            start = idx + 1
            backtrack(arr,idx+1, start)
            arr.pop()

            # have the current letter be part of some other substring
            start = oldStart
            backtrack(arr,idx+1,start)

        backtrack([],0,0)
        return res
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l= 0
        smallDic = Counter(s1)
        dic = defaultdict(int)

        l = 0
        match = 0
        for r in range(len(s2)):
            if r-l+1 <= len(s1):
                dic[s2[r]] += 1
                if(s2[r] in smallDic and dic[s2[r]] == smallDic[s2[r]]):
                    match += 1        
                continue

            if match == len(smallDic):
                return True
            
            let = s2[l]
            
            if (let in smallDic) and dic[let] == smallDic[let]:
                match -= 1

            dic[let] -= 1
            

            l += 1
            
            let = s2[r]
            dic[let] += 1
            if((let in smallDic) and dic[let] == smallDic[let]):
                match += 1

            
        
        print(match)
        print(len(smallDic))
        return match == len(smallDic)


            
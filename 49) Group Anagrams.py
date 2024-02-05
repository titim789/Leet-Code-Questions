class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        ana = []
        length = len(strs)
        
        for i in range(length):
            temp = [x for x in strs[i]]
            temp.sort()
            if temp in ana:
                ans[ana.index(temp)].append(strs[i])
            else:
                ans.append([strs[i]])
                ana.append(temp)
        return ans

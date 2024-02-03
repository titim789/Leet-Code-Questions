class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []
        stack = [[0,0,""]]
        while stack != []:
            l, r, string = stack.pop()
            
            if len(string) == n*2:
                a.append(string)
                continue
            if l < n:
                stack.append([l+1, r, string+"("])
                
            if l > r:
                stack.append([l,r+1,string+")"])
        return a
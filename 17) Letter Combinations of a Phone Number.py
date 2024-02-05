class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        def getCombi(d, digits):
            if len(digits) == 1:
                return d[digits]
            a = getCombi(d, digits[:len(digits)-1])
            b = []
            for i in a:
                for j in d[digits[-1]]:
                    b.append(i+j)
            return b
    
        return getCombi(d, digits)
            
            
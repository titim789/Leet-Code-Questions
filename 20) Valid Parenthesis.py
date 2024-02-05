class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for c in s:
            if c in ["(","[","{"]:
                l.append(c)
            elif len(l) == 0:
                return False
            elif c == ")":
                if l[-1] == "(":
                    l = l[:-1]
                else:
                    return False
            elif c == "]":
                if l[-1] == "[":
                    l = l[:-1]
                else:
                    return False
            elif c == "}":
                if l[-1] == "{":
                    l = l[:-1]
                else:
                    return False
        if len(l) != 0:
            return False
        return True
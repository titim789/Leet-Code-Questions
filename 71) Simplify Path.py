class Solution:
    def simplifyPath(self, path: str) -> str:
        path_elem = path.split("/")
        ans = []
        for elem in path_elem:
            if elem == "" or elem == ".":
                continue
            else:
                if elem == "..":
                    if ans:
                        ans.pop()
                else:
                    ans.append(elem)
        
        return "/"+"/".join(ans)
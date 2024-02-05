class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        st = []
        pl = []
        for c in s:
            if st == [] and c == ")":
                pl.append(0)
                continue
            else:
                if c == "(":
                    st.append(c)
                    pl.append(1)

                else:
                    # print(st, pl)
                    if st[-1] == "(":
                        for i in range(len(pl)-1, -1, -1):
                            if pl and pl[i] == 0:
                                continue
                            elif pl[i] == 1:
                                pl[i] = 2
                                break
                        st.pop()
        # print(st, pl)
        mx = count = 0
        for i in pl:
            if i == 2:
                count += 1
            else:
                if count > mx:
                    mx = count
                count = 0

        if count > mx:
            mx = count*2
        else:
            mx *= 2

        return mx
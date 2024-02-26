class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        letters = list(t)
        lettersLeft = {"total":len(t)}
        letterQueue = []
        minLength = [-1,-1,10**5]

        for i in range(len(t)):
            if t[i] in lettersLeft:
                lettersLeft[t[i]] += 1
            else:
                lettersLeft[t[i]] = 1

        # print(lettersLeft)
        for i in range(len(s)):
            # print(s[i])
            found = False
            for letter in range(len(letters)):
                if letters[letter] == s[i]:
                    found = True
                    break
            if not found:
                continue
            else:
                for x in range(len(letterQueue)):
                    if letterQueue[x][0] == s[i]:
                        if lettersLeft[s[i]] == 0:
                            del letterQueue[x]
                        break
                letterQueue.append([s[i], i])
                if lettersLeft[s[i]] != 0:
                    lettersLeft[s[i]] -= 1
                    lettersLeft["total"] -= 1
            # print(lettersLeft, letterQueue)

            if lettersLeft['total'] == 0:
                currDist = letterQueue[-1][1] - letterQueue[0][1]
                if currDist < minLength[2]:
                    minLength = [letterQueue[0][1],letterQueue[-1][1], currDist]
                lettersLeft[letterQueue[0][0]] += 1
                lettersLeft["total"] += 1
                letterQueue = letterQueue[1:]
                # print("POP",currDist, lettersLeft, letterQueue)

        if minLength[0] == -1:
            return ""
        else:
            # print(minLength)
            return s[minLength[0]:] if minLength[1]+1 == len(s) else s[minLength[0]:minLength[1]+1]
        
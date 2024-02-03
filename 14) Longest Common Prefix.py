class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for i in range(1,len(strs)):
            temp = ""
            for word_index in range(len(word)):
                if word_index >= len(strs[i]):
                    break
                if word[word_index] == strs[i][word_index]:
                    temp += word[word_index]
                else:
                    break
            if temp == "":
                return ""
            else:
                word = temp
        return word
        
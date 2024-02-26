class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)
        if length1 == 0 or length2 == 0:
            return length1 if length2 == 0 else length2
        memo = [[None if i != 0 and j != 0 else i if i > j else j for i in range(length2+1)] for j in range(length1+1)]

        for w1 in range(length1):
            for w2 in range(length2):
                if word1[w1] == word2[w2]:
                    memo[w1+1][w2+1] =memo[w1][w2]
                else:
                    memo[w1+1][w2+1] = min(memo[w1+1][w2]+1, memo[w1][w2+1]+1, memo[w1][w2]+1)
        
        return memo[-1][-1]
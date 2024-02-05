class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        def top(mat):
            for i in mat[0]:
                ans.append(i)
            return mat[1:]
        
        def right(mat):
            last_index = len(mat[0])-1
            for i in mat:
                ans.append(i[last_index])
            return [x[:-1] for x in mat]
        
        def btm(mat):
            for i in mat[-1][::-1]:
                ans.append(i)
            return mat[:-1]
        
        def left(mat):
            for i in mat[::-1]:
                ans.append(i[0])
            return [x[1:] for x in mat]
        
        temp = matrix.copy()
        inter = 0
        while temp:
            # print(temp)
            # print(ans)
            for i in range(len(temp))[::-1]:
                if temp[i] == []:
                    del temp[i]
            if temp == []:
                break
            if inter%4 == 0:
                temp=top(temp)
            elif inter%4 == 1:
                temp=right(temp)
            elif inter%4 == 2:
                temp=btm(temp)
            else:
                temp=left(temp)
            inter += 1

        return ans
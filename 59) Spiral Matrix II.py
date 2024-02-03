class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[i for i in range(n)] for i in range(n)]
        
        top = 0
        right = n-1
        btm = n-1
        left = 0
        curr = "top"
        curr_num = 1

        while curr_num < n*n+1:
            if curr == "top":
                for i in range(left, right+1):
                    ans[top][i] = curr_num
                    curr_num += 1
                curr = "right"
                top += 1

            elif curr == "right":
                for i in range(top, btm+1):
                    ans[i][right] = curr_num
                    curr_num += 1
                curr = "btm"
                right -= 1

            elif curr == "btm":
                for i in range(right, left-1, -1):
                    ans[btm][i] = curr_num
                    curr_num += 1
                curr = "left"
                btm -= 1
            else: #curr == left
                for i in range(btm, top-1, -1):
                    ans[i][left] = curr_num
                    curr_num += 1
                curr = "top"
                left += 1
        
        return ans
        
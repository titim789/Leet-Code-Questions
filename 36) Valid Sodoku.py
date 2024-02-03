class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = []
            t = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in t:
                        return False
                    t.append(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in s:
                        return False
                    s.append(board[j][i])
        
        for i in [1,4,7]:
            for j in [1,4,7]:
                u = []
                for k in range(-1,2):
                    for l in range(-1,2):
                        if board[i+k][j+l] != ".":
                            if board[i+k][j+l] in u:
                                return False
                            u.append(board[i+k][j+l])
        return True
                    
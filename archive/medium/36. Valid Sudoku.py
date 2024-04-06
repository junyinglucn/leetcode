class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in s:
                        s.remove(board[i][j])
                    else:
                        return False
        for i in range(9):
            s = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for j in range(9):
                if board[j][i] == ".":
                    continue
                else:
                    if board[j][i] in s:
                        s.remove(board[j][i])
                    else:
                        return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] == ".":
                            continue
                        else:
                            if board[i + k][j + l] in s:
                                s.remove(board[i + k][j + l])
                            else:
                                return False
        return True

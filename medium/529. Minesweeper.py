class Solution:
    def updateBoard(self, board, click):
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        def check(i, j):
            count = 0
            for x, y in direction:
                x, y = x + i, y + j
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "M":
                    count += 1
            return count

        def dfs(i, j):
            ct = check(i, j)
            if not ct:
                board[i][j] = "B"
                for x, y in direction:
                    x, y = x + i, y + j
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "E":
                        dfs(x, y)
            else:
                board[i][j] = str(ct)

        dfs(click[0], click[1])
        return board

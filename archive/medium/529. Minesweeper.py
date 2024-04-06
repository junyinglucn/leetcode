# Solution A
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

# Solution B
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]):
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]

        m = len(board)
        n = len(board[0])

        def in_board(x, y):
            return 0 <= x < m and 0 <= y < n

        def bfs(x, y):
            signed = [[False] * n for _ in range(m)]
            signed[x][y] = True
            from collections import deque
            queue = deque()
            queue.append([x, y])

            while queue:
                count = 0
                x, y = queue.popleft()
                if board[x][y] == 'M':
                    board[x][y] = 'X'
                    return
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if in_board(nx, ny) and board[nx][ny] == 'M':
                        count += 1
                if count > 0:
                    board[x][y] = str(count)
                else:
                    board[x][y] = 'B'
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if in_board(nx, ny) and signed[nx][ny] != True:
                            queue.append([nx, ny])
                            signed[nx][ny] = True

        x, y = click
        bfs(x, y)
        return board
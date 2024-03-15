n,m,t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0,-1, 0] #하우상좌
dy = [0, 1, 0, -1]
wind = []

for i in range(n):
    for j in range(m):
        if board[i][j] == -1:
            wind.append([i,j])
def spreadDust():
    newboard = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 0:
                spread = board[i][j] // 5
                cnt = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != -1:
                        newboard[ni][nj] += spread
                        cnt += 1
                newboard[i][j] -= (cnt * spread)

    for i in range(n):
        for j in range(m):
            board[i][j] += newboard[i][j]

def cleanUpDust():
    i0, j0 = wind[0]
    newboard = [[-2]*m for _ in range(n)]
    i,j, dir = 0,0,0
    while True:
        ni = i + dx[dir]
        nj = j + dy[dir]
        if newboard[ni][nj] != -2:
            break
        newboard[ni][nj] = board[i][j]
        if ni in [0, i0] and nj in [0, m-1]:
            dir = (dir + 1) %4
        i, j = ni, nj
    for i in range(n):
        for j in range(m):
            if newboard[i][j] != -2 and board[i][j] != -1:
                if newboard[i][j] == -1:
                    board[i][j] = 0
                else:
                    board[i][j] = newboard[i][j]
def cleanLowDust():
    wind0, wind1 = wind
    i0, j0 = wind0
    i1, j1 = wind1
    newboard = [[-2]*m for _ in range(n)]
    i,j, dir = i1, 0,1
    while True:
        ni = i + dx[dir]
        nj = j + dy[dir]
        if newboard[ni][nj] != -2:
            break

        newboard[ni][nj] = board[i][j]
        if ni in [i1, n-1] and nj in [0, m-1]:
            dir = (dir - 1) %4
        i, j = ni, nj
    for i in range(n):
        for j in range(m):
            if newboard[i][j] != -2 and board[i][j] != -1:
                if newboard[i][j] == -1:
                    board[i][j] = 0
                else:
                    board[i][j] = newboard[i][j]


for time in range(t):
    spreadDust()
    cleanUpDust()
    cleanLowDust()

ans = 0
for i in range(n):
    ans += sum(board[i])

print(ans +2)
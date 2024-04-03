n,m =map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
movingrules = [list(map(int, input().split())) for _ in range(m)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]

nurish = [[0]*n for _ in range(n)]
for i in range(n-2,n):
    for j in range(2):
        nurish[i][j] = 1

def movenurish(d, p):
    moved = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if nurish[i][j] == 1:
                ni, nj = (i+dx[d]*p)%n, (j+dy[d]*p)%n
                board[ni][nj] += 1
                moved[ni][nj] = 1
    newboard = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if moved[i][j] == 1:
                for dir in range(2,9,2):
                    ni_, nj_ = i+dx[dir], j+dy[dir]
                    if 0<=ni_<n and 0<=nj_<n:
                        if board[ni_][nj_] >=1:
                            newboard[i][j]+=1

    for i in range(n):
        for j in range(n):
            board[i][j] += newboard[i][j]

    return moved

def cutTree():
    newnurish =[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not nurish[i][j] and board[i][j] >=2:
                board[i][j] -= 2
                newnurish[i][j] = 1

    return newnurish

for move in movingrules:
    d, p = move
    nurish = movenurish(d, p)
    nurish = cutTree()

ans = 0
for i in range(n):
    ans += sum(board[i])
print(ans)
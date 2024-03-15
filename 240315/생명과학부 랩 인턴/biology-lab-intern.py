n,m,k = map(int, input().split())
gompang = [list(map(int,input().split())) for _ in range(k)]

dx = [-1, 1, 0, 0] #위 아래 오른쪽 왼쪽
dy = [0, 0, 1, -1]

board = [[] for _ in range(n)]

for i in range(n):
    for j in range(m):
        board[i].append([])

for idx, gp in enumerate(gompang):
    x,y,s,d,b = gp
    board[x-1][y-1].append(idx)
    gompang[idx] = [s, d-1, b]

def catchGP(j):
    global ans
    for i in range(n):
        if board[i][j] != []:
            idx = board[i][j].pop()
            ans += gompang[idx][2]
            gompang[idx] = []
            break

def moveGP():
    newGP = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != []:
                idx = board[i][j].pop()
                gs,gd,gb = gompang[idx]
                ni, nj = i, j
                for dist in range(gs):
                    ni += dx[gd]
                    nj += dy[gd]
                    if ni<0 or ni>=n or nj<0 or nj>=m:
                        if gd % 2 == 0:
                            gd += 1
                        else:
                            gd -= 1
                        ni += dx[gd]*2
                        nj += dy[gd]*2
                gompang[idx] = [gs,gd,gb]
                newGP.append([idx,ni,nj])

    for idx, x, y in newGP:
        if board[x][y] != []:
            org = gompang[board[x][y][0]][2]
            new = gompang[idx][2]
            if org < new:
                board[x][y] = [idx]
        else:
            board[x][y].append(idx)

ans = 0
for sy in range(m):
    catchGP(sy)
    moveGP()
print(ans)
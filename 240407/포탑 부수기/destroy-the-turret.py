from collections import deque

n,m,k=map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
atkboard = [[0]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def selectAtk(now):
    si, sj, sp, st = -1,-1, 10e9, -1
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                if (sp, st, -(si+sj), -sj) > (board[i][j], -atkboard[i][j], -(i+j), -j):
                    si, sj, sp = i, j, board[i][j]

    atkboard[si][sj] = now
    board[si][sj] += n+m

    ti, tj, tp, tt = -1, 10e9, -1, 10e9
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and [i,j] != [si,sj]:
                if (tp, -tt, -(ti+tj), -tj) < (board[i][j], -atkboard[i][j], -(i+j), -j):
                    ti, tj, tp, tt = i, j, board[i][j], atkboard[i][j]

    atkResult = lazerAtk([si,sj], [ti,tj])
    if atkResult == []:
        atkResult = bombAtk([si,sj], [ti,tj])

    for i in range(n):
        for j in range(m):
            if board[i][j] <0:
                board[i][j] = 0
            if board[i][j] != 0 and not atkResult[i][j]:
                board[i][j] += 1
                


def lazerAtk(atk, tar):
    ai, aj = atk
    ti, tj = tar
    q= deque()
    q.append([ti,tj])
    visited = [[0]*m for _ in range(n)]
    visited[ti][tj] = 1
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx,ny = (x+dx[d])%n, (y+dy[d])%m
            if visited[nx][ny] ==0 and board[nx][ny] !=0:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx,ny])

    if visited[ai][aj] == 0:
        return []

    i,j = ai, aj
    attacked = [[0]*m for _ in range(n)]
    while True:
        for d in range(4):
            ni = (i+dx[d])%n
            nj = (j+dy[d])%m
            if visited[ni][nj] == visited[i][j] -1:
                i, j = ni, nj
                break
        if [i,j] == [ti, tj]:
            break
        attacked[i][j] = 1


    board[ti][tj] -= board[ai][aj]
    for x in range(n):
        for y in range(m):
            if attacked[x][y] == 1:
                board[x][y] -= (board[ai][aj]//2)
            if [x,y] == atk or [x,y] == tar:
                attacked[x][y] = 1

    return attacked

def bombAtk(atk, tar):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1] #상 _ 좌 _ 하 _ 우 _
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    ai, aj = atk
    ti, tj = tar
    attacked = [[0]*m for _ in range(n)]
    for d in range(8):
        ni, nj = (ti+dx[d])%n, (tj+dy[d])%m
        if board[ni][nj] != 0:
            attacked[ni][nj] = 1

    board[ti][tj] -= board[ai][aj]
    for x in range(n):
        for y in range(m):
            if attacked[x][y] == 1:
                board[x][y] -= (board[ai][aj]//2)
            if [x,y] == atk or [x,y] == tar:
                attacked[x][y] = 1

    return attacked

for turn in range(1,k+1):
    selectAtk(turn)
    dead = 0
    for i in range(n):
        dead += board[i].count(0)
    if dead == (n*m)-1:
        break
ans = 0
for i in range(n):
    ans = max(ans, max(board[i]))
print(ans)
from collections import deque
n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

attack = [[0]*m for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def selectAtk(turn):
    si,sj = -1,-1
    atk = 10e9
    tar = -1
    ti, tj = -1,-1
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                if (atk, -attack[si][sj], -(si+sj), -sj) > (board[i][j], -attack[i][j], -(i+j), -j):
                    atk = board[i][j]
                    si, sj = i,j
                if (tar, -attack[ti][tj], -(ti + tj), -tj) < (board[i][j], -attack[i][j], -(i + j), -j):
                    tar = board[i][j]
                    ti, tj = i, j
    board[si][sj] += n+m
    Attack([si,sj], [ti,tj])
    attack[si][sj] = turn

def Attack(attacker, target):
    ai,aj = attacker
    ti, tj = target
    q = deque()
    q.append([ti,tj])
    visited = [[0]*m for _ in range(n)]
    visited[ti][tj] = 1
    attacked = [[0]*m for _ in range(n)]
    attacked[ai][aj] = 1
    attacked[ti][tj] = 1
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = (x+dx[d])%n
            ny = (y+dy[d])%m
            if not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx,ny])

    if visited[ai][aj] ==0:
        attacked = bombAttack(attacker, target)
    else:
        value = board[ai][aj]
        q = deque()
        q.append([ai,aj])
        while q:
            x,y = q.popleft()
            dist = visited[x][y]
            for d in range(4):
                nx,ny = (x+dx[d])%n, (y+dy[d])%m
                if [nx,ny] == [ti, tj]:
                    board[nx][ny] -= value
                    break
                if visited[nx][ny] == visited[x][y] -1:
                    q.append([nx,ny])
                    attacked[nx][ny] = 1
                    board[nx][ny] -= (value//2)
                    break

    for i in range(n):
        for j in range(m):
            if attacked[i][j] == 0 and board[i][j]:
                board[i][j] += 1

def bombAttack(atk, tar):
    ai, aj = atk
    ti, tj = tar
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,-1,-1,-1,0,1,1,1]

    attacked = [[0]*m for _ in range(n)]
    attacked[ai][aj] = 1
    attacked[ti][tj] = 1
    value = board[ai][aj]
    board[ti][tj] -= value
    for d in range(8):
        ni,nj = (ti+dx[d])%n, (tj+dy[d])%m
        if board[ni][nj]:
            attacked[ni][nj] = 1
            board[ni][nj] -= (value//2)
    return attacked


for turn in range(1, k+1):
    selectAtk(turn)
    cnt = 0
    for i in range(n):
        cnt += board[i].count(0)
    if cnt >= (n**2) -1:
        break
        
ans = 0
for i in range(n):
    ans = max(ans, max(board[i]))
print(ans)
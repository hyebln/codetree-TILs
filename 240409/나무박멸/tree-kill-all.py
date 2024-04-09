import copy

n,m,k,c = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
dead = [[0]*n for _ in range(n)]

def growTree():
    newTree= copy.deepcopy(board)
    emtpycnt = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]> 0:
                for d in range(4):
                    ni,nj = i+dx[d], j+dy[d]
                    if 0<=ni<n and 0<=nj<n:
                        if board[ni][nj] > 0:
                            newTree[i][j] += 1
                        if board[ni][nj] == 0 and not dead[ni][nj]:
                            emtpycnt[i][j] += 1
                            
    for i in range(n):
        for j in range(n):
            if emtpycnt[i][j]:
                spread = newTree[i][j] // emtpycnt[i][j]
                for d in range(4):
                    ni,nj = i+dx[d], j+dy[d]
                    if 0<=ni<n and 0<=nj<n and board[ni][nj] == 0 and not dead[ni][nj]:
                        newTree[ni][nj] += spread

    return newTree

def deadTree():
    global ans
    dx = [-1, 1, 1, -1]
    dy = [-1, -1, 1, 1]
    deadcnt = [[0]*n for _ in range(n)]
    select, maxdead = [-1,-1], 0
    for i in range(n):
        for j in range(n):
            if board[i][j]>0:
                deadcnt[i][j] += board[i][j]
                for d in range(4):
                    for dist in range(1,k+1):
                        ni,nj = i+dx[d]*dist, j+dy[d]*dist
                        if 0<=ni<n and 0<=nj<n:
                            if board[ni][nj] <= 0:
                                break
                            deadcnt[i][j] += board[ni][nj]

                if (maxdead, -select[0], -select[1]) < (deadcnt[i][j], -i, -j):
                    maxdead = deadcnt[i][j]
                    select = [i,j]

    if select == [-1,-1]:
        return
    si, sj = select
    ans += board[si][sj]
    board[si][sj] = 0
    dead[si][sj] = c+1
    for d in range(4):
        for dist in range(1, k+1):
            ni,nj = si+dx[d]*dist, sj+dy[d]*dist
            if 0<=ni<n and 0<=nj<n:
                if board[ni][nj] == -1:
                    break
                if board[ni][nj] == 0:
                    dead[ni][nj] = c+1
                    break
                ans += board[ni][nj]
                dead[ni][nj] = c+1
                board[ni][nj] = 0


ans = 0
for year in range(m):
    board = growTree()
    deadTree()
    for i in range(n):
        for j in range(n):
            if dead[i][j]:
                dead[i][j] -=1

print(ans)
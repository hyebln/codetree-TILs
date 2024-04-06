import copy

n,m,k,c = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

deadboard = [[0]*n for _ in range(n)]
def growTree():
    newboard= copy.deepcopy(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                spread = []
                cnt = 0
                for d in range(4):
                    ni,nj = i+dx[d], j+dy[d]
                    if 0<=ni<n and 0<=nj<n:
                        if board[ni][nj] > 0:
                            newboard[i][j] += 1
                        if board[ni][nj] == 0 and deadboard[ni][nj] == 0:
                            cnt += 1
                            spread.append([ni,nj])
                if cnt != 0:
                    spreadtree = newboard[i][j] // cnt
                    for si, sj in spread:
                        newboard[si][sj] += spreadtree
    return newboard


def startDead():
    global ans
    dx = [-1, -1, 1, 1]
    dy = [1, -1, 1, -1]
    maxdead = -1
    maxlist = [[n,n]]
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                deadcnt = board[i][j]
                deadlist = [[i,j]]
                for d in range(4):
                    for dist in range(1, k+1):
                        ni, nj = i + dx[d]*dist, j + dy[d]*dist
                        if ni<0 or ni>=n or nj<0 or nj>=n:
                            break
                        if board[ni][nj] > 0:
                            deadcnt += board[ni][nj]
                            deadlist.append([ni,nj])
                        if board[ni][nj] == 0:
                            deadlist.append([ni,nj])
                            break
                        if board[ni][nj] == -1:
                            break
                if (deadcnt, -deadlist[0][0], -deadlist[0][1]) > (maxdead, -maxlist[0][0], -maxlist[0][1]):
                    maxdead = deadcnt
                    maxlist = deadlist

    if maxdead == -1:
        return
    for di, dj in maxlist:
        board[di][dj] = 0
        deadboard[di][dj] = c+1

    ans += maxdead




ans = 0
for year in range(m):
    board = growTree()
    startDead()
    for i in range(n):
        for j in range(n):
            if deadboard[i][j]>1:
                deadboard[i][j] -= 1
            else:
                deadboard[i][j] = 0
print(ans)
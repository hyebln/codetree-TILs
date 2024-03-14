from collections import  deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            robot = [i, j, 2]
            board[i][j] = 0

dx = [0, 0, 1, -1] #동서남북
dy = [1, -1, 0, 0]

def findMonster(r):
    ri,rj,rl = r
    distboard = [[0]*n for _ in range(n)]
    q = deque()
    q.append([ri,rj])
    distboard[ri][rj] = 1
    monst = [[0,0,10e9]]
    while q:
        x,y = q.popleft()
        dist = distboard[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n and not distboard[nx][ny] and board[nx][ny]<=rl:
                q.append([nx,ny])
                distboard[nx][ny] = dist +1
                if 1<=board[nx][ny]<rl:
                    if monst[0][2] > dist+1:
                        monst[0] = [nx, ny, dist+1]
                    elif monst[0][2] == dist+1:
                        monst.append([nx,ny,dist+1])
    monst.sort(key=lambda x:[x[0], x[1]])
    return monst[0]

def eatMonster(m):
    global eating, robot
    mi, mj, md = m
    board[mi][mj] = 0
    eating += 1
    robot[0] = mi
    robot[1] = mj
    if eating == robot[2]:
        eating = 0
        robot[2] += 1

eating = 0
time = 0
while True:
    selected = findMonster(robot)
    if selected[2] == 10e9:
        break
    else:
        eatMonster(selected)

    time += selected[2]-1
print(time)
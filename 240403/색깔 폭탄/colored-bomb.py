from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def groupbomb():
    global ans
    visited = [[0]*n for _ in range(n)]
    biggest = []
    biggestinfo = [10e9, -1, 10e9]
    for i in range(n):
        for j in range(n):
            if visited[i][j] or board[i][j] <= 0:
                continue
            q = deque()
            q.append([i,j])
            visited[i][j] = 1
            group = [[i,j]]
            groupinfo = [0, 0, 0] #red,행,열
            color = board[i][j]
            while q:
                x,y = q.popleft()
                for d in range(4):
                    nx, ny = x +dx[d], y+dy[d]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny] in [0, color] and [nx,ny] not in group:
                        q.append([nx,ny])
                        group.append([nx,ny])
                        if board[nx][ny] == 0:
                            groupinfo[0] +=1
                        if board[nx][ny] == color:
                            visited[nx][ny] = 1
                            if (groupinfo[1], -groupinfo[2]) < (nx, -ny):
                                groupinfo[1], groupinfo[2] = nx, ny

            if len(group) < 2:
                continue
            if (len(biggest), -biggestinfo[0], biggestinfo[1], -biggestinfo[2]) < (len(group), -groupinfo[0], groupinfo[1], -groupinfo[2]):
                biggest = group
                biggestinfo = groupinfo
    for i,j in biggest:
        board[i][j] = -5
    ans += len(biggest)**2

    return len(biggest)

def gravity(board):
    newboard = [[-5]*n for _ in range(n)]
    for j in range(n):
        lastidx = n-1
        for i in range(n-1, -1, -1):
            if board[i][j] == -5:
                continue
            if board[i][j] == -1:
                lastidx = i
            newboard[lastidx][j] = board[i][j]
            lastidx -= 1
    return newboard

ans = 0
cnt = 0
while True:
    find = groupbomb()
    if not find:
        break
    board1 = gravity(board)
    rotateboard = list(map(list, zip(*board1)))[::-1]
    board = gravity(rotateboard)

print(ans)
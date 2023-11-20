from collections import deque
n,m,k= map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
people = []
for _ in range(m):
    x,y = map(int, input().split())
    people.append([x-1,y-1])
ex, ey = map(int,input().split())
ex -= 1
ey -= 1
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
def Move():
    global ans
    for idx in range(len(people)):
        px,py = people[idx]
        if [px,py] == [-1,-1]:
            continue
        dist = abs(px - ex) + abs(py-ey)
        move = False
        for d in range(4):
            nx,ny = px+dx[d], py+dy[d]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] ==0:
                ndist = abs(nx - ex) + abs(ny-ey)
                if ndist<dist:
                    move = [nx,ny]
                    break
        if move:
            ans += 1
            people[idx] = move
            if move == [ex,ey]:
                people[idx] = [-1,-1]
def Rotate():
    global ex, ey
    size = 1
    rec = []
    for px, py in people:
        if [px,py] == [-1,-1]:
            continue
        board[px][py] += 10
    board[ex][ey] = -1
    while not rec:
        for i in range(n-1):
            for j in range(n-1):
                if i <= ex<=i+size and j<=ey<=j+size:
                    for px,py in people:
                        if i <= px <= i+size and j <= py <= j+size:
                            rec = [i,j, i+size, j+size]
                            break
                if rec:
                    break
            if rec:
                break
        size += 1
    turnboard = [listt[rec[1]:rec[3]+1] for listt in board[rec[0]:rec[2]+1]]
    turned = list(map(list, zip(*turnboard[::-1])))
    for i in range(rec[0],rec[2]+1):
        for j in range(rec[1], rec[3]+1):
            ti, tj = i-rec[0], j-rec[1]
            if 0<turned[ti][tj]<10:
                board[i][j] = turned[ti][tj] -1
            else:
                board[i][j] = turned[ti][tj]
    newpeople = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                ex, ey = i,j
                board[i][j] = 0
            if board[i][j] > 9 :
                num = board[i][j] // 10
                for _ in range(num):
                    newpeople.append([i,j])
                board[i][j] = 0
    return newpeople

for time in range(k):
    Move()
    if people.count([-1,-1]) == len(people):
        break
    people = Rotate()
print(ans)
print(ex+1, ey+1)
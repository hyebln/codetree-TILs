from collections import deque, defaultdict
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def makeGroup():
    global ans
    groupboard = [[0]*n for _ in range(n)]
    groupinfo = defaultdict(list) #숫자, 갯수
    gidx = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] and not groupboard[i][j]:
                gidx += 1
                q = deque()
                q.append([i,j])
                groupboard[i][j] = gidx
                number = board[i][j]
                groupinfo[gidx] = [number,1]
                while q:
                    x,y = q.popleft()
                    for d in range(4):
                        nx,ny = x+dx[d], y+dy[d]
                        if 0<=nx<n and 0<=ny<n and board[nx][ny]==number and not groupboard[nx][ny]:
                            groupboard[nx][ny] = gidx
                            q.append([nx,ny])
                            groupinfo[gidx][1] += 1
    besides = defaultdict(list)
    for _ in range(1,gidx+1):
        besides[_] = [0]*(gidx+1)

    for i in range(n):
        for j in range(n):
            idx = groupboard[i][j]
            for d in range(4):
                ni,nj = i+dx[d], j+dy[d]
                if 0<=ni<n and 0<=nj<n and groupboard[ni][nj] != idx:
                    nidx = groupboard[ni][nj]
                    besides[idx][nidx] += 1

    total = 0
    for idx in range(1,gidx+1):
        for nidx in range(idx+1, gidx+1):
            score = (groupinfo[idx][1] + groupinfo[nidx][1]) * groupinfo[idx][0]*groupinfo[nidx][0]*besides[idx][nidx]
            total += score
    ans += total

def rotateBoard():
    newboard = [[0]*n for _ in range(n)]
    for i in range(n):
        newboard[i][n//2] = board[i][n//2]
        newboard[n//2][i] = board[n//2][i]

    newboard = list(map(list, zip(*newboard)))[::-1]
    for i in range(0,n, n//2+1):
        for j in range(0, n, n//2+1):
            small=[[0]*(n//2) for _ in range(n//2)]
            for di in range(n//2):
                for dj in range(n//2):
                    small[di][dj] = board[i+di][j+dj]

            turnedsmall = list(map(list, zip(*small[::-1])))
            for di in range(n//2):
                for dj in range(n//2):
                    newboard[i+di][j+dj] = turnedsmall[di][dj]

    return newboard

ans = 0
makeGroup()
for turn in range(3):
    board = rotateBoard()
    makeGroup()
print(ans)
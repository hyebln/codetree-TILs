from collections import deque

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dice = [[1,6],[4,3],[2,5]] #상하, 좌우, 앞뒤

dx = [0, 1, 0, -1] # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

def moveDice(d, diceloc):
    di, dj = diceloc
    ni, nj = di+dx[d], dj+dy[d]
    if ni<0 or ni>=n or nj<0 or nj>=n:
        d = (d+2)%4
        ni, nj = di + dx[d], dj + dy[d]

    if d ==0:
        dice[0], dice[1] = dice[1], dice[0][::-1]

    elif d == 1:
        dice[0], dice[2] = dice[2][::-1], dice[0]

    elif d == 2:
        dice[0], dice[1] = dice[1][::-1], dice[0]

    elif d == 3:
        dice[0], dice[2] = dice[2], dice[0][::-1]
    return d, [ni,nj]

def getScore():
    global ans
    si, sj = diceloc
    q = deque()
    q.append([si,sj])
    visited = [[0]*n for _ in range(n)]
    visited[si][sj] = 1
    ans += board[si][sj]
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == board[si][sj]:
                q.append([nx,ny])
                visited[nx][ny] = 1
                ans += board[nx][ny]

ans = 0
dir = 0
diceloc = [0, 0]
for move in range(m):
    dir, diceloc = moveDice(dir, diceloc)
    getScore()
    if dice[0][1] > board[diceloc[0]][diceloc[1]]:
        dir = (dir+1) %4
    elif dice[0][1] < board[diceloc[0]][diceloc[1]]:
        dir = (dir+3)%4

print(ans)
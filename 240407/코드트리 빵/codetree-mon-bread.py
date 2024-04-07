from collections import defaultdict, deque
n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
conv = [[]]
for _ in range(m):
    x,y =map(int,input().split())
    conv.append([x-1,y-1])
personloc = defaultdict(list)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def movePerson():
    arrive = []
    for idx, loc in personloc.items():
        if loc == [-1, -1]:
            continue
        x,y = loc
        cx, cy = conv[idx]
        q = deque()
        q.append([cx,cy])
        visited = [[0]*n for _ in range(n)]
        visited[cx][cy] = 1
        while q:
            i,j = q.popleft()
            for d in range(4):
                ni, nj = i+dx[d], j+dy[d]
                if 0<=ni<n and 0<=nj<n and visited[ni][nj] == 0 and board[ni][nj] != -1:
                    visited[ni][nj] = visited[i][j]+1
                    q.append([ni,nj])

        g, gx, gy, gd = 10e9, 0, 0, 5
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny] == 0:
                continue
            if (g, gd) > (visited[nx][ny], d):
                g, gd, gx,gy = visited[nx][ny], d, nx,ny
        personloc[idx] = [gx,gy]

        if [gx,gy] == conv[idx]:
            personloc[idx] = [-1, -1]
            arrive.append([gx,gy])

    for x,y in arrive:
        board[x][y] = -1


def findBC(t):
    ci, cj = conv[t]
    q = deque()
    q.append([ci,cj])
    visited = [[0]*n for _ in range(n)]
    visited[ci][cj] = 1
    mind = 10e9
    target = [-1,-1]
    while q:
        x,y = q.popleft()
        dist = visited[x][y]
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if board[nx][ny] == 1:
                    visited[nx][ny] = dist+1
                    if (mind, target[0], target[1]) > (dist + 1, nx, ny):
                        mind = dist + 1
                        target = [nx, ny]

                elif board[nx][ny] >=0:
                    visited[nx][ny] = dist + 1
                    q.append([nx,ny])

    board[target[0]][target[1]] = -1
    personloc[t] = [target[0],target[1]]


time = 1
findBC(time)
while True:
    time += 1
    movePerson()
    if time <=m:
        findBC(time)
    personloclist = list(personloc.values())
    if personloclist.count([-1,-1]) == m:
        break

print(time)
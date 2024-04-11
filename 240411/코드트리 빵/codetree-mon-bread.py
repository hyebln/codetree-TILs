from collections import deque, defaultdict

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
conv = [[]]
for _ in range(m):
    x,y = map(int,input().split())
    conv.append([x-1,y-1])
dx = [-1,0,0,1]
dy = [0,-1,1,0]
personloc = defaultdict(list)

def goBasecamp(idx):
    ci, cj = conv[idx]
    q = deque()
    q.append([ci, cj])
    visited = [[0]*n for _ in range(n)]
    visited[ci][cj] = 1
    basecamp = [10e9, -1,-1]
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx,ny = x +dx[d], y+dy[d]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] != -1:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx,ny])
                if board[nx][ny] == 1:
                    if (basecamp[0], basecamp[1], basecamp[2]) > (visited[nx][ny], nx, ny):
                        basecamp = [visited[nx][ny], nx,ny]

    personloc[idx] = [basecamp[1], basecamp[2]]
    board[basecamp[1]][basecamp[2]] = -1

def movePerson():
    arrived = []
    for idx, loc in personloc.items():
        if loc == []:
            continue
        pi, pj = loc
        ci, cj = conv[idx]
        q = deque()
        q.append([ci, cj])
        visited = [[0]*n for _ in range(n)]
        visited[ci][cj] = 1
        while q:
            x,y = q.popleft()
            for d in range(4):
                nx,ny = x +dx[d], y+dy[d]
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] != -1:
                    visited[nx][ny] = visited[x][y]+1
                    q.append([nx,ny])

        next = [10e9, -1,-1]
        for d in range(4):
            ni, nj = pi+dx[d], pj+dy[d]
            if 0<=ni<n and 0<=nj<n and next[0] > visited[ni][nj] and board[ni][nj] != -1:
                next = [visited[ni][nj], ni, nj]

        if [next[1], next[2]] == [ci,cj]:
            personloc[idx] = []
            arrived.append([ci,cj])
        else:
            personloc[idx] = [next[1], next[2]]

    for x,y in arrived:
        board[x][y] = -1

time = 1
goBasecamp(time)
while True:
    time += 1
    movePerson()
    if time <=m:
        goBasecamp(time)
        
    if list(personloc.values()).count([]) == m:
        print(time)
        break
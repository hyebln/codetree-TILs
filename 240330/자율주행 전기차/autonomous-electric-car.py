from collections import deque
n,m,c = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tx,ty = map(int,input().split())
tx -= 1
ty -= 1
start, end = [], []
for i in range(m):
    info = list(map(int,input().split()))
    start.append([info[0]-1, info[1]-1])
    end.append([info[2]-1, info[3]-1])
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def findPassenger():
    global c
    q = deque()
    q.append([tx,ty])
    visited = [[0]*n for _ in range(n)]
    visited[tx][ty] = 1
    si, sj, sd = 10e9,10e9,10e9
    if [tx, ty] in start:
        idx = start.index([tx,ty])
        return idx
    while q:
        i,j = q.popleft()
        dist= visited[i][j]
        for d in range(4):
            ni, nj = i+dx[d], j+dy[d]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj] == 0 and not board[ni][nj]:
                visited[ni][nj] = dist + 1
                q.append([ni,nj])
                if [ni,nj] in start and (sd,si,sj)>=(dist+1, ni,nj):
                    si, sj, sd = ni,nj,dist+1

    if c < sd-1:
        return 'impossible'
    c -= sd-1
    idx = start.index([si,sj])
    return idx

def moveTaxi(idx):
    global tx, ty, c
    si, sj = start.pop(idx)
    ei, ej = end.pop(idx)
    q = deque()
    q.append([si,sj])
    visited = [[0]*n for _ in range(n)]
    visited[si][sj] = 1
    stop = False
    while q:
        if stop:
            break
        i,j = q.popleft()
        dist= visited[i][j]
        for d in range(4):
            ni, nj = i+dx[d], j+dy[d]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj] == 0 and not board[ni][nj]:
                visited[ni][nj] = dist + 1
                if ni==ei and nj==ej:
                    stop = True
                q.append([ni,nj])
    needed = visited[ei][ej]-1
    if needed == -1:
        return True
    if c < needed:
        return True
    c += needed
    tx, ty = ei, ej
    return False


while True:
    pidx = findPassenger()
    if type(pidx) != int:
        print(-1)
        break
    result = moveTaxi(pidx)

    if result:
        print(-1)
        break

    if start ==[] and end ==[]:
        print(c)
        break
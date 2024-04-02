from collections import deque, defaultdict


n,q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(2**n)]
rotatelevel = list(map(int,input().split()))

def splitBoard(l):
    for x in range(0,2**n,2**l):
        for y in range(0,2**n, 2**l):
            splitboard = [i[y:y+2**l] for i in board[x:x+2**l]]
            rotate = rotateBoard(splitboard)
            for i in range(x, x+2**l):
                for j in range(y, y+2**l):
                    board[i][j] = rotate[i-x][j-y]


def rotateBoard(org):
    l = len(org)
    rotated = [[0]*l for _ in range(l)]
    rec = 0
    dx = [0, l//2, -(l//2), 0]
    dy = [l//2, 0, 0, -(l//2)]
    for x in range(0, l, l//2):
        for y in range(0, l, l//2):
            for nx in range(x,x+(l//2)):
                for ny in range(y, y+(l//2)):
                    rotated[nx+dx[rec]][ny+dy[rec]] = org[nx][ny]
            rec += 1
    return rotated

def meltingIce():
    newboard = [[3]*2**n for _ in range(2**n)]
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    for i in range(2**n):
        for j in range(2**n):
            for d in range(4):
                ni, nj = i +dx[d], j+dy[d]
                if 0<=ni<2**n and 0<=nj<2**n and board[ni][nj]>0:
                    newboard[i][j] -= 1

    for i in range(2 ** n):
        for j in range(2 ** n):
            if board[i][j] ==0:
                continue
            if newboard[i][j]>0:
                board[i][j] -= 1

def calgroup():
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    visited = [[0]*2**n for _ in range(2**n)]
    group = 1
    groupdict = defaultdict(int)
    for i in range(2**n):
        for j in range(2**n):
            if not visited[i][j] and board[i][j] > 0:
                q=deque()
                q.append([i,j])
                visited[i][j] = group
                groupdict[group] = 1
                while q:
                    x,y = q.popleft()
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if 0<=nx<2**n and 0<=ny<2**n and board[nx][ny]>0 and not visited[nx][ny]:
                            visited[nx][ny] = group
                            groupdict[group] += 1
                            q.append([nx,ny])
                group += 1
    if len(groupdict.values())>0:
        return max(groupdict.values())
    else:
        return 0

for rlevel in rotatelevel:
    if rlevel != 0:
        splitBoard(rlevel)
    meltingIce()
    # break
ans1 = 0
for i in range(2**n):
    for j in range(2**n):
        ans1 += board[i][j]

print(ans1)
print(calgroup())
from collections import deque, defaultdict

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
def makeGroup():
    global ans
    grouped = [[0]*n for _ in range(n)]
    q = deque()
    gnum = 0
    gcnt = [0]
    gcolor = [0]
    for i in range(n):
        for j in range(n):
            if grouped[i][j] != 0:
                continue
            gnum += 1
            cnt = 1
            q.append([i,j])
            grouped[i][j] = gnum
            gcolor.append(board[i][j])
            while q:
                x,y= q.popleft()
                color = board[x][y]

                for d in range(4):
                    nx, ny = x+dx[d], y +dy[d]
                    if 0 <=nx<n and 0<=ny<n and grouped[nx][ny] == 0:
                        if board[nx][ny] == color:
                            grouped[nx][ny] = gnum
                            q.append([nx,ny])
                            cnt += 1
            gcnt.append(cnt)


    besidedict = defaultdict(list)
    for i in range(gnum+1):
        besidedict[i] = [0]*(gnum+1)

    for x in range(n):
        for y in range(n):
            gidx = grouped[x][y]
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if grouped[nx][ny] != gidx:
                        gidx_ = grouped[nx][ny]
                        besidedict[gidx][gidx_] += 1

    score1 = 0
    for a in range(1, gnum+1):
        for b in range(a, gnum+1):
            beauty = (gcnt[a]+gcnt[b])*gcolor[a]*gcolor[b]*besidedict[a][b]
            score1 += beauty
    ans += score1

def turnBoard():
    crossline = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == n//2 or j == n//2:
                crossline[i][j] = board[i][j]

    crossline_ = list(map(list, zip(*crossline)))[::-1]
    for i in [0, n//2+1]:
        for j in [0, n//2+1]:
            sepboard =[[0]*(n//2) for _ in range(n//2)]
            for di in range(n//2):
                for dj in range(n//2):
                    sepboard[di][dj] = board[di+i][dj+j]

            sepboard_ = list(map(list,zip(*sepboard[::-1])))
            for di in range(n//2):
                for dj in range(n//2):
                    crossline_[di+i][dj+j] = sepboard_[di][dj]

    return crossline_

ans = 0
makeGroup()
for step in range(3):
    board = turnBoard()
    makeGroup()
print(ans)
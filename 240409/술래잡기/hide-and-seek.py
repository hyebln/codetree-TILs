n,m,h,k = map(int, input().split())
catcher = [n//2, n//2]

runners = [[[] for _ in range(n)] for i in range(n)]
for _ in range(m):
    x,y,d = map(int,input().split())
    if d == 1:
        runners[x-1][y-1].append(0)
    elif d == 2:
        runners[x-1][y-1].append(1)

tree = [[0]*n for _ in range(n)]
for _ in range(h):
    x,y = map(int,input().split())
    tree[x-1][y-1] = 1

dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]


clockwise = [[0]*n for _ in range(n)]
counterclock = [[0]*n for _ in range(n)]
def initCatcher():
    si,sj,sd = n//2, n//2, 3
    clockwise[si][sj] = sd
    counterclock[si][sj] = sd
    dist = 1
    while dist<=n:
        for t in range(2):
            for _ in range(dist):
                si += dx[sd]
                sj += dy[sd]
                if 0<=si<n and 0<=sj<n:
                    clockwise[si][sj] = sd
                    counterclock[si][sj] = (sd+2)%4
            sd = (sd+1)%4
            if 0<=si<n and 0<=sj<n:
                clockwise[si][sj] = sd
        dist += 1
    clockwise[0][0] = 1
    counterclock[0][0] = 1

def moveRunner():
    ci, cj = catcher
    newboard = [[[] for _ in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            dist = abs(ci-i)+abs(cj-j)
            if dist > 3:
                continue
            if runners[i][j] != []:
                for d in runners[i][j]:
                    ni,nj = i+dx[d], j+dy[d]
                    if 0<=ni<n and 0<=nj<n:
                        if [ni,nj] == catcher:
                            newboard[i][j].append(d)
                        else:
                            newboard[ni][nj].append(d)
                    else:
                        d = (d+2)%4
                        ni,nj = i+dx[d], j+dy[d]
                        if [ni,nj] == catcher:
                            newboard[i][j].append(d)
                        else:
                            newboard[ni][nj].append(d)

    return newboard



def moveCatcher(clockdir):
    ci, cj = catcher
    if clockdir:
        cd = clockwise[ci][cj]
        ni,nj = ci+dx[cd], cj+dy[cd]
        viewd = clockwise[ni][nj]
    else:
        cd = counterclock[ci][cj]
        ni,nj = ci+dx[cd], cj+dy[cd]
        viewd= counterclock[ni][nj]

    catcher[0], catcher[1] = ni,nj
    catchRunner(ni,nj,viewd)



def catchRunner(x,y,d):
    global ans
    catchnum = 0
    for dist in range(3):
        nx = x+dx[d]*dist
        ny = y+dy[d]*dist
        if 0<=nx<n and 0<=ny<n and not tree[nx][ny]:
            if runners[nx][ny] != []:
                catchnum += len(runners[nx][ny])
                runners[nx][ny] = []
    ans += catchnum*(turn+1)

ans = 0
clockdir = True
initCatcher()
for turn in range(k):
    runners = moveRunner()
    moveCatcher(clockdir)
    if catcher == [0,0] or catcher == [n//2,n//2]:
        clockdir = not clockdir

print(ans)
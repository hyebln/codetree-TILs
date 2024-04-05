n,m,h,k = map(int,input().split())
runner = [list(map(int, input().split())) for _ in range(m)]
tree = [list(map(int,input().split())) for _ in range(h)]
runboard = [[[] for i in range(n)] for _ in range(n)]
treeboard = [[0]*n for _ in range(n)]
ci, cj, cd = n//2, n//2, 3
dx = [0, 1, 0, -1] #우 하 좌 상
dy = [1, 0, -1, 0]
for run in runner:
    x,y,d = run
    runboard[x-1][y-1].append(d-1)

for t in tree:
    x,y = t
    treeboard[x-1][y-1] = 1


clockwise = [[0] * n for _ in range(n)]
counterclockwise = [[0] * n for _ in range(n)]
i, j, cd = ci, cj, 3
clockwise[i][j] = cd
counterclockwise[i][j] = cd
dist = 1
while dist <= n:
    for _ in range(2):
        for dd in range(dist):
            i += dx[cd]
            j += dy[cd]
            if 0 <= i < n and 0 <= j < n:
                clockwise[i][j] = cd
                counterclockwise[i][j] = (cd + 2) % 4
        cd = (cd + 1) % 4
        if 0 <= i < n and 0 <= j < n:
            clockwise[i][j] = cd
    dist += 1

def moveRunner():
    newboard = [[[] for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if runboard[i][j] != []:
                for idx in range(len(runboard[i][j])):
                    dir = runboard[i][j][idx]
                    dist = abs(i-ci) + abs(j-cj)
                    if dist <=3:
                        ni,nj = i+dx[dir], j +dy[dir]
                        if 0<=ni<n and 0<=nj<n:
                            if [ni,nj] == [ci, cj]:
                                newboard[i][j].append(dir)
                                continue
                            else:
                                newboard[ni][nj].append(dir)
                        else:
                            dir = (dir + 2)%4
                            ni, nj = i + dx[dir], j + dy[dir]
                            if [ni,nj] != [ci, cj]:
                                newboard[ni][nj].append(dir)
                            else:
                                newboard[i][j].append(dir)
                    else:
                        newboard[i][j].append(dir)
    return newboard

def moveCatcher(t, ci, cj):
    global ans
    if ((t+1) // (n**2))%2 == 0 :
        cd = clockwise[ci][cj]
        ni, nj = ci+dx[cd], cj+dy[cd]
        view = clockwise[ni][nj]
    else:
        cd = counterclockwise[ci][cj]
        ni, nj = ci+dx[cd], cj+dy[cd]
        view = counterclockwise[ni][nj]
    vi, vj = ni, nj
    while True:
        vi += dx[view]
        vj += dy[view]
        if vi<0 or vi >=n or vj<0 or vj>=n:
            break
        if treeboard[vi][vj]:
            continue
        if runboard[vi][vj] != []:
            ans += len(runboard[vi][vj])*(t+1)
            runboard[vi][vj] = []


    return ni,nj


ans = 0
for turn in range(k):
    runboard = moveRunner()
    ci, cj= moveCatcher(turn, ci, cj)
print(ans)
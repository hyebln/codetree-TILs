n,m,h,k = map(int,input().split())
runnerboard = [[[] for i in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,d = map(int,input().split())
    runnerboard[x-1][y-1].append(d-1)

treeboard = [[0]*n for _ in range(n)]
for _ in range(h):
    x,y = map(int,input().split())
    treeboard[x-1][y-1] =1

dx = [0, 1, 0, -1] #우하좌상
dy = [1, 0, -1, 0]
ci, cj = n//2, n//2
clockwise = [[0]*n for _ in range(n)]
counterclock = [[0]*n for _ in range(n)]

def setinit():
    dist = 1
    si, sj, sd = ci, cj, 3
    clockwise[ci][cj] = 3

    while dist <= n:
        for _ in range(2):
            for dst in range(dist):
                si += dx[sd]
                sj += dy[sd]
                if 0<=si<n and 0<=sj<n:
                    clockwise[si][sj] = sd
                    counterclock[si][sj] = (sd+2)%4
            sd = (sd+1)%4
            if 0<=si<n and 0<=sj<n:
                clockwise[si][sj] = sd
                counterclock[si][sj] = (sd+1)%4

        dist += 1
    clockwise[0][0] = 1
    counterclock[ci][cj] = 3


def moveRunner():
    newrunner = [[[] for _ in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if runnerboard[i][j] != []:
                if abs(i-ci)+abs(j-cj) >3:
                    newrunner[i][j].extend(runnerboard[i][j])
                    continue
                for rd in runnerboard[i][j]:
                    ni, nj = i+dx[rd], j+dy[rd]
                    if 0<=ni<n and 0<=nj<n:
                        if [ni,nj] == [ci,cj]:
                            newrunner[i][j].append(rd)
                        else:
                            newrunner[ni][nj].append(rd)

                    else:
                        rd_ = (rd+2)%4
                        ni,nj = i+dx[rd_], j+dy[rd_]
                        if [ni,nj] == [ci,cj]:
                            newrunner[i][j].append(rd_)
                        else:
                            newrunner[ni][nj].append(rd_)
                            
    return newrunner

def moveCatcher(clock, i,j):
    if clock:
        cd = clockwise[i][j]
        ni, nj = i+dx[cd], j+dy[cd]
        viewd = clockwise[ni][nj]
    else:
        cd = counterclock[i][j]
        ni, nj = i+dx[cd], j+dy[cd]
        viewd = counterclock[ni][nj]

    if [ni,nj] in [[0,0], [n//2, n//2]]:
        clock = not clock

    vi, vj = ni, nj

    catch = 0
    for _ in range(3):
        vi = ni + dx[viewd]*_
        vj = nj + dy[viewd]*_
        if vi<0 or vi>=n or vj<0 or vj>=n:
            break
        if treeboard[vi][vj]:
            continue
        if runnerboard[vi][vj]:
            cnt = len(runnerboard[vi][vj])
            runnerboard[vi][vj] = []
            catch += cnt

    return clock, ni, nj, catch
setinit()
clock = True
ans=0
for turn in range(k):
    runnerboard = moveRunner()
    clock, ci, cj, catch = moveCatcher(clock, ci, cj)
    ans += catch*(turn+1)
print(ans)
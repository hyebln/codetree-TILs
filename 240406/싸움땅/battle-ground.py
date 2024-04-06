from collections import defaultdict
n,m,k = map(int,input().split())
gunboard= [[[] for i in range(n)] for j in range(n)]
for i in range(n):
    listt = list(map(int, input().split()))
    for j in range(n):
        a = listt.pop(0)
        if a == 0:
            continue
        gunboard[i][j].append(a)

playerboard = [[0]*n for _ in range(n)]
players = defaultdict(list)
point = defaultdict(int)
for idx in range(m):
    x,y,d,s = map(int,input().split())
    playerboard[x-1][y-1] = idx+1
    players[idx+1] = [x-1, y-1, d,s,0]
    point[idx+1] = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def movePlayer():
    for idx in range(1,m+1):
        px,py,pd,ps,pg = players[idx]
        nx,ny = px+dx[pd], py+dy[pd]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            pd = (pd+2)%4
            nx,ny = px+dx[pd], py+dy[pd]

        if playerboard[nx][ny] >0:
            idx2 = playerboard[nx][ny]
            playerboard[px][py] = 0
            players[idx] = [nx,ny, pd,ps,pg]
            fightPlayer(nx, ny, idx, idx2)

        elif playerboard[nx][ny] == 0:
            if gunboard[nx][ny] != []:
                gunboard[nx][ny].sort()
                maxg = gunboard[nx][ny].pop(-1)
                if maxg > pg:
                    players[idx] = [nx,ny,pd,ps,maxg]
                    if pg > 0:
                        gunboard[nx][ny].append(pg)
                else:
                    players[idx] = [nx, ny, pd,ps,pg]
                    gunboard[nx][ny].append(maxg)
                playerboard[nx][ny] = idx
                playerboard[px][py] = 0
            else:
                playerboard[nx][ny] = idx
                playerboard[px][py] = 0
                players[idx] = [nx,ny,pd,ps,pg]

def fightPlayer(x,y,p1,p2):
    x1,y1,d1,s1,g1 = players[p1]
    x2,y2,d2,s2,g2 = players[p2]
    if (s1+g1, s1) > (s2+g2, s2):
        point[p1] += (s1+g1)-(s2+g2)
        Loser(x,y,p2)
        Winner(x,y,p1)

    if (s1+g1, s1) < (s2+g2, s2):
        Loser(x,y,p1)
        Winner(x,y,p2)
        point[p2] += (s2+g2)-(s1+g1)


def Winner(x,y,pidx):
    i,j,d,s,g = players[pidx]
    if gunboard[x][y] == []:
        players[pidx] = [x,y,d,s,g]
        playerboard[x][y] = pidx
    else:
        gunboard[x][y].sort()
        maxg = gunboard[x][y].pop(-1)
        if maxg > g:
            players[pidx] = [x,y,d,s,maxg]
            gunboard[x][y].append(g)
        else:
            gunboard[x][y].append(maxg)
            players[pidx] = [x,y,d,s,g]
        playerboard[x][y] = pidx


def Loser(x,y,pidx):
    i,j,d,s,g = players[pidx]
    if g > 0:
        gunboard[x][y].append(g)
    while True:
        nx, ny = x+dx[d], y+dy[d]
        if 0<=nx<n and 0<=ny<n and playerboard[nx][ny] == 0:
            break
        d = (d+1)%4

    if gunboard[nx][ny] == []:
        players[pidx] = [nx,ny,d,s,0]
        playerboard[nx][ny] = pidx

    else:
        gunboard[nx][ny].sort()
        maxg = gunboard[nx][ny].pop(-1)
        players[pidx] = [nx, ny, d, s, maxg]
        playerboard[nx][ny] = pidx

for round in range(k):
    movePlayer()
print(*list(point.values()))
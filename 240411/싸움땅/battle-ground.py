from collections import defaultdict
n,m,k=map(int,input().split())
gunboard = []
for i in range(n):
    guns = [[i] for i in list(map(int,input().split()))]
    gunboard.append(guns)
players = defaultdict(list)
playerboard =[[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(m):
    x,y,d,s = map(int,input().split())
    playerboard[x-1][y-1] = _+1
    players[_+1]=[x-1,y-1,d,s,0]
pscore = [0]*(m+1)

def movePlayer():
    for idx, player in players.items():
        px,py,pd,ps,pg = player
        playerboard[px][py] = 0
        nx,ny = px+dx[pd], py+dy[pd]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            pd = (pd+2)%4
            nx,ny = px+dx[pd], py+dy[pd]
        if not playerboard[nx][ny]:
            playerboard[nx][ny] = idx
            if gunboard[nx][ny]:
                gunboard[nx][ny].sort()
                maxg =gunboard[nx][ny].pop(-1)
                if pg<maxg:
                    players[idx] = [nx,ny,pd,ps,maxg]
                    gunboard[nx][ny].append(pg)
                else:
                    players[idx] = [nx,ny,pd,ps,pg]
                    gunboard[nx][ny].append(maxg)
            else:
                players[idx] = [nx,ny,pd,ps,pg]
        else:
            fidx = playerboard[nx][ny]
            playerboard[nx][ny]=0
            fx,fy,fd,fs,fg = players[fidx]
            if (ps+pg, ps) < (fs+fg, fs):
                pscore[fidx] += (fs+fg-ps-pg)
                gunboard[nx][ny].append(pg)
                playerboard[nx][ny] = fidx
                Loser(idx, nx,ny,pd,ps)
                Winner(fidx, fx,fy,fd,fs,fg)
            else:
                pscore[idx] += (ps+pg-fs-fg)
                gunboard[nx][ny].append(fg)
                playerboard[nx][ny] = idx
                Loser(fidx, fx,fy,fd,fs)
                Winner(idx, nx,ny,pd,ps,pg)
                
def Loser(idx, x,y,d,s):
    while True:
        nx,ny = x+dx[d], y+dy[d]
        if 0<=nx<n and 0<=ny<n and not playerboard[nx][ny]:
            break
        d = (d+1)%4

    playerboard[nx][ny] = idx
    if gunboard[nx][ny]:
        gunboard[nx][ny].sort()
        maxg = gunboard[nx][ny].pop(-1)
        players[idx] = [nx,ny,d,s,maxg]
    else:
        players[idx] = [nx,ny,d,s,0]

def Winner(idx, x,y,d,s,g):
    gunboard[x][y].sort()
    maxg = gunboard[x][y].pop(-1)
    if g<maxg:
        players[idx] = [x,y,d,s,maxg]
        gunboard[x][y].append(g)
    else:
        players[idx] = [x,y,d,s,g]
        gunboard[x][y].append(maxg)


for rounds in range(k):
    movePlayer()
print(*pscore[1:])
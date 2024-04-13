import copy

m,t = map(int,input().split())
packman = list(map(int,input().split()))
packman[0] -= 1
packman[1] -= 1
mboard = [[[] for _ in range(4)] for i in range(4)]
dead = [[0]*4 for _ in range(4)]
for _ in range(m):
    r,c,d = map(int,input().split())
    mboard[r-1][c-1].append(d-1)

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1] #↑, ↖, ←, ↙, ↓, ↘, →, ↗

def monsterMove():
    newboard = [[[] for _ in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            if mboard[i][j]:
                for d in mboard[i][j]:
                    cantgo = False
                    nd = d
                    cnt = 0
                    while True:
                        ni,nj = i+dx[nd], j+dy[nd]
                        if cnt ==8:
                            cantgo = True
                        if 0<=ni<4 and 0<=nj<4 and not dead[ni][nj] and [ni,nj] != packman:
                            break
                        nd = (nd+1)%8
                        cnt += 1
                    if cantgo:
                        newboard[i][j].append(d)
                    else:
                        newboard[ni][nj].append(nd)
    return newboard

def packmanMove():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    moveloc = []
    maxeat = -1
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                dlist = [d1,d2,d3]
                eat = 0
                pi, pj = packman
                visited = []
                for _ in range(3):
                    pi += dx[dlist[_]]
                    pj += dy[dlist[_]]
                    if pi <0 or pi>=4 or pj<0 or pj>=4 or [pi,pj] in visited:
                        break
                    if mboard[pi][pj]:
                        eat += len(mboard[pi][pj])
                        visited.append([pi,pj])
                if maxeat < eat:
                    moveloc = visited
                    maxeat = eat

    for pi,pj in moveloc:
        if mboard[pi][pj]:
            mboard[pi][pj] = []
            dead[pi][pj] = 3
    packman[0], packman[1] = pi, pj

for turn in range(1,t+1):
    orgmonster = copy.deepcopy(mboard)
    mboard = monsterMove()
    packmanMove()
    for i in range(4):
        for j in range(4):
            if dead[i][j] > 0:
                dead[i][j] -= 1
            mboard[i][j] += orgmonster[i][j]

ans = 0
for i in range(4):
    for j in range(4):
       ans += len(mboard[i][j])

print(ans)
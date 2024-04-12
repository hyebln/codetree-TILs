n,m,p,C,D = map(int,input().split())
ludolph = list(map(int,input().split()))
ludolph[0] -= 1
ludolph[1] -= 1
santalist = [[] for _ in range(p+1)]
score = [0]*(p+1)
for _ in range(p):
    idx, r,c = map(int,input().split())
    santalist[idx] = [r-1,c-1]
stun = [0]*(p+1)

def moveLudolph():
    dx = [-1,0,1,0, -1,1,1,-1]
    dy = [0,1,0,-1, 1,1,-1,-1]
    lx, ly = ludolph
    mindist = 10e9
    select = [-1,-1,-1]
    for sidx in range(p+1):
        if santalist[sidx] == []:
            continue
        sx, sy = santalist[sidx]
        dist = (sx-lx)**2 + (sy-ly)**2
        if (mindist, -select[0], -select[1]) > (dist, -sx, -sy):
            mindist = dist
            select = [sx,sy, sidx]

    si, sj, sidx = select
    dist = (lx-si)**2 + (ly-sj)**2
    nextludolph = [-1,-1, -1]
    for d in range(8):
        lx_, ly_ = lx+dx[d], ly+dy[d]
        if lx_<0 or lx_ >=n or ly_<0 or ly_ >=n:
            continue
        dist_ = (lx_-si)**2 + (ly_-sj)**2
        if dist > dist_:
            dist = dist_
            nextludolph = [lx_, ly_, d]

    ludolph[0], ludolph[1] = nextludolph[:2]
    if nextludolph[:2] in santalist:
        sidx = santalist.index(nextludolph[:2])
        score[sidx] += C
        stun[sidx] += 2

        lx, ly, ld = nextludolph
        nx, ny = lx+dx[ld]*C, ly+dy[ld]*C
        if nx<0 or nx >=n or ny<0 or ny>=n:
            santalist[sidx] = []
        else:
            if [nx,ny] in santalist:
                interaction(sidx, ld, [nx,ny])
            else:
                santalist[sidx] = [nx,ny]



def moveSanta():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    li, lj = ludolph
    for idx in range(1, p+1):
        if santalist[idx] == [] or stun[idx]:
            continue
        si, sj = santalist[idx]
        mindist = (si-li)**2 + (sj-lj)**2
        nextsanta = [-1,-1, -1]
        for d in range(4):
            ni, nj =si+dx[d], sj+dy[d]
            if 0<=ni<n and 0<=nj<n and [ni,nj] not in santalist:
                dist = (ni-li)**2 + (nj-lj)**2
                if mindist > dist:
                    mindist= dist
                    nextsanta = [ni,nj, d]

        if nextsanta[:2] == ludolph:
            score[idx] += D
            stun[idx] = 2

            nx, ny, nd = nextsanta
            nd = (nd+2)%4
            nx_, ny_ = nx+dx[nd]*D, ny+dy[nd]*D
            if nx_<0 or nx_ >=n or ny_<0 or ny>=n:
                santalist[idx] = []
            else:
                if [nx_,ny_] in santalist:
                    if santalist.index([nx_,ny_]) == idx:
                        santalist[idx] = [nx_, ny_]
                        continue
                    interaction(idx, nd, [nx_,ny_])
                else:
                    santalist[idx] = [nx_,ny_]

        elif nextsanta[:2] != [-1,-1]:
            santalist[idx] = nextsanta[:2]

def interaction(newidx, d, sloc):
    dx = [-1,0,1,0, -1,1,1,-1]
    dy = [0,1,0,-1, 1,1,-1,-1]
    
    x,y = sloc
    orgidx = santalist.index(sloc)
    movelist = [sloc]
    moveidx = [newidx, orgidx]
    while True:
        nx, ny = x+dx[d], y+dy[d]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            break
        x, y = nx, ny
        movelist.append([nx, ny])
        if [nx,ny] in santalist:
            moveidx.append(santalist.index([nx,ny]))
            
    for i in range(len(moveidx)):
        idx = moveidx[i]
        if i < len(movelist):
            santalist[idx] = movelist[i]
        else:
            santalist[idx] = []

for turn in range(1, 1+m):
    moveLudolph()
    if santalist.count([]) == p+1:
        break
    moveSanta()
    for idx in range(1, p+1):
        if santalist[idx] != []:
            score[idx] += 1
        if stun[idx] > 0:
            stun[idx] -= 1

print(*score[1:])
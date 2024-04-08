n,m,p,C,D = map(int,input().split())
ludolph = list(map(int,input().split()))
ludolph[0] -= 1
ludolph[1] -= 1
santa = [[] for _ in range(p+1)]
gizul = [0]*(p+1)
score = [0]*(p+1)

for i in range(p):
    idx, r,c = map(int,input().split())
    santa[idx] = [r-1,c-1]

def moveLudolph():
    li,lj = ludolph
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,-1,-1,-1,0,1,1,1]
    nearsanta = [10e9, -1,-1, -1]
    for idx in range(p+1):
        if santa[idx] == []:
            continue
        si, sj = santa[idx]
        dist = (si-li)**2 + (sj-lj)**2
        if (nearsanta[0], -nearsanta[1], -nearsanta[2]) > (dist, -si, -sj):
            nearsanta = [dist, si, sj, idx]
            
    sdist, si, sj, sidx = nearsanta
    ldir = 0
    for d in range(8):
        ni,nj = li+dx[d], lj+dy[d]
        if 0<=ni<n and 0<=nj<n:
            dist = (ni-si)**2 + (nj-sj)**2
            if sdist > dist:
                sdist = dist
                ldir = d

    ludolph[0], ludolph[1] = li+dx[ldir], lj+dy[ldir]
    if ludolph == [si, sj]:
        score[sidx] += C
        crushLudolph(si,sj,ldir,sidx)

def moveSanta():
    dx = [-1, 0, 1, 0]  # 상우하좌
    dy = [0, 1, 0, -1]
    li,lj = ludolph
    for idx in range(p+1):
        if santa[idx] == [] or gizul[idx]:
            continue
        si,sj = santa[idx]
        move_d, mindist = -1, ((li-si)**2+(lj-sj)**2)
        for d in range(4):
            ni,nj = si+dx[d], sj + dy[d]
            if 0<=ni<n and 0<=nj<n and [ni,nj] not in santa:
                dist = (ni-li)**2 + (nj-lj)**2
                if mindist > dist:
                    move_d = d
                    mindist = dist

        if move_d == -1:
            continue
        si_, sj_ = si+dx[move_d], sj+dy[move_d]
        if [si_, sj_] == ludolph:
            score[idx] += D
            crushSanta(si_, sj_, move_d, idx)

        else:
            santa[idx] = [si_,sj_]


def crushLudolph(i,j,d,sidx):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    ni, nj = i+dx[d]*C, j+dy[d]*C

    if ni<0 or ni>=n or nj<0 or nj>=n:
        santa[sidx] = []
        return
    gizul[sidx] = 2
    if [ni,nj] in santa:
        org_idx =sidx
        si, sj = ni, nj
        while True:
            newidx = santa.index([si,sj])
            santa[org_idx] = [si,sj]
            si += dx[d]
            sj += dy[d]
            org_idx = newidx
            if si<0 or si>=n or sj<0 or sj>=n:
                break
            if [si,sj] not in santa:
                santa[org_idx] = [si,sj]
                break

    else:
        santa[sidx] = [ni,nj]


def crushSanta(i,j,d, sidx):
    dx = [-1, 0, 1, 0]  # 상우하좌
    dy = [0, 1, 0, -1]
    d = (d+2)%4
    ni, nj = i+dx[d]*D, j+dy[d]*D
    if ni<0 or ni>=n or nj<0 or nj>=n:
        santa[sidx] = []
        return

    gizul[sidx] = 2
    if [ni,nj] in santa:
        org_idx =sidx
        si, sj = ni, nj
        while True:
            newidx = santa.index([si,sj])
            santa[org_idx] = [si,sj]
            si += dx[d]
            sj += dy[d]
            org_idx = newidx
            print(si, sj)
            if si<0 or si>=n or sj<0 or sj>=n:
                break
            if [si,sj] not in santa:
                santa[org_idx] = [si,sj]
                break

    else:
        santa[sidx] = [ni,nj]



for turn in range(m):
    moveLudolph()
    moveSanta()

    for _ in range(p+1):
        if gizul[_]:
            gizul[_] -= 1
        if santa[_] != []:
            score[_] += 1
            
for i in range(1, p+1):
    print(score[i], end =' ')
import copy
from collections import defaultdict
l,n,q = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(l)]
person = [[]]
for _ in range(n):
    r,c,h,w,k = map(int,input().split())
    person.append([r-1,c-1,h,w,k])

movelist = [list(map(int,input().split())) for _ in range(q)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

orgperson = copy.deepcopy(person)
def moveKnight(m):
    knightboard = [[0]*l for _ in range(l)]
    for idx in range(1,n+1):
        if person[idx] == []:
            continue
        r,c,h,w,k = person[idx]
        for r_ in range(h):
            for c_ in range(w):
                knightboard[r+r_][c+c_] = idx

    mi, md = m
    moveidx = set()
    moveidx.add(mi)
    moved = [[0]*l for _ in range(l)]
    while moveidx:
        midx = moveidx.pop()
        i, j, h, w, k = person[midx]
        for di in range(h):
            for dj in range(w):
                i_, j_ = i+di, j+dj
                ni,nj = i_+dx[md], j_+dy[md]
                if ni<0 or ni>=l or nj<0 or nj>=l:
                    return
                moved[ni][nj] = midx
                if knightboard[ni][nj] != midx and knightboard[ni][nj] > 0:
                    moveidx.add(knightboard[ni][nj])

    cantgo = False
    for i in range(l):
        for j in range(l):
            if moved[i][j] and board[i][j] == 2:
                cantgo = True

    if cantgo:
        return
    else:
        getDamage(moved, mi)

def getDamage(movedboard, org):
    check = [0]*(n+1)
    for i in range(l):
        for j in range(l):
            if movedboard[i][j]:
                idx = movedboard[i][j]
                if person[idx] == []:
                    continue
                if not check[idx]:
                    person[idx][0], person[idx][1] = i, j
                    check[idx] = True
                if board[i][j] == 1 and idx != org:
                    person[idx][-1] -= 1
                    if person[idx][-1] == 0:
                        person[idx] = []

ans = 0
for turn in range(q):
    move = movelist[turn]
    moveKnight(move)

    
for idx in range(n+1):
    if person[idx]:
        orgk = orgperson[idx][-1]
        newk = person[idx][-1]
        ans += (orgk-newk)
print(ans)
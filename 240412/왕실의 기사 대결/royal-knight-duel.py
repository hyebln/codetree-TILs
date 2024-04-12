from collections import defaultdict, deque
l,n,q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(l)]
knight = defaultdict(list)
orgknight =defaultdict(list)
for _ in range(1, n+1):
    r,c,h,w,k = map(int,input().split())
    knight[_] = [r-1,c-1,h,w,k]
    orgknight[_] = [r-1,c-1,h,w,k]
queries = [list(map(int,input().split())) for _ in range(q)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def moveKnight(idx,d):
    knightboard = [[0]*l for _ in range(l)]
    for id, kn in knight.items():
        if kn == []:
            continue
        x,y,h,w,k = kn
        for i in range(x,x+h):
            for j in range(y,y+w):
                knightboard[i][j] = id

    q = deque()
    q.append(idx)
    visited = [[0]*l for _ in range(l)]
    cant_go = False
    while q:
        cidx = q.popleft()
        si, sj, sh, sw, sk = knight[cidx]
        for i in range(si, si+sh):
            for j in range(sj, sj+sw):
                ni, nj = i+dx[d], j+dy[d]
                if ni<0 or ni>=l or nj<0 or nj>=l:
                    cant_go = True
                else:
                    visited[ni][nj] = cidx
                    if knightboard[ni][nj] > 0 and knightboard[ni][nj] != cidx:
                        nidx = knightboard[ni][nj]
                        if nidx not in q:
                            q.append(nidx)
            if cant_go:
                break
                
    if cant_go:
        return

    damage = [0]*(n+1)
    for i in range(l):
        for j in range(l):
            if visited[i][j] and board[i][j] == 2:
                cant_go = True
                return
            if visited[i][j] and board[i][j] == 1:
                kidx = visited[i][j]
                damage[kidx] += 1

    damage[idx] = 0
    moved = defaultdict(list)
    for i in range(l):
        for j in range(l):
            if visited[i][j]:
                kidx = visited[i][j]
                if not moved[kidx]:
                    moved[kidx] = [i,j]
                    
    for idx, loc in moved.items():
        ki,kj,kh,kw,kk = knight[idx]
        nk = kk-damage[idx]
        if nk <= 0:
            knight[idx] = []
        else:
            knight[idx] = [loc[0],loc[1], kh,kw,kk-damage[idx]]
            

for query in queries:
    idx, d = query
    moveKnight(idx,d)

ans = 0
for idx, kn in knight.items():
    if kn == []:
        continue
    orgk = orgknight[idx][-1]
    newk = kn[-1]
    ans += (orgk-newk)
print(ans)
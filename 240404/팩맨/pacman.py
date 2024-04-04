m,t = map(int,input().split())
r,c = map(int,input().split())
pi, pj = r-1, c-1
Monster = [list(map(int, input().split())) for _ in range(m)]
monsterboard = [[[],[],[],[]] for _ in range(4)]
deadboard = [[[],[],[],[]] for _ in range(4)]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1] #↑, ↖, ←, ↙, ↓, ↘, →, ↗
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


for monster in Monster:
    r,c,d = monster
    monsterboard[r-1][c-1].append(d)

def moveMonster(monsterboard):
    newboard = [[[],[],[],[]] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mdlist = monsterboard[i][j]
            if len(mdlist) >0 :
                for md in mdlist:
                    tcnt = 0
                    while True:
                        ni, nj = i + dx[md], j + dy[md]
                        if ni<0 or ni >=4 or nj<0 or nj>=4 or len(deadboard[ni][nj]) > 0 or [ni,nj] == [pi,pj]:
                            md = (md+1)%9
                            if md == 0:
                                md += 1
                            tcnt +=1
                            if tcnt >= 8:
                                break
                        else:
                            break
                    newboard[ni][nj].append(md)

    return monsterboard, newboard


def movePackman(board):
    global pi, pj
    dx = [-1, 0, 1, 0] #상좌하우
    dy = [0, -1, 0, 1]
    maxeat = [0,[]] #cnt,route
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                ni,nj = pi, pj
                eatable = [0, []]
                visited = [[0]*4 for _ in range(4)]
                skip = False
                for dd in [d1, d2,d3]:
                    ni += dx[dd]
                    nj += dy[dd]
                    if ni<0 or ni>=4 or nj<0 or nj>=4 or visited[ni][nj]:
                        skip = True
                        continue
                    visited[ni][nj] = 1
                    eatable[0] += len(board[ni][nj])
                    eatable[1].append([ni,nj])
                if skip:
                    continue
                if maxeat[0] < eatable[0]:
                    maxeat = eatable

    for mi,mj in maxeat[1]:
        if board[mi][mj] == []:
            continue
        board[mi][mj] = []
        if -3 not in deadboard[mi][mj]:
            deadboard[mi][mj].append(-3)

    pi,pj = maxeat[1][2]

    return board

for turn in range(t):
    org, new = moveMonster(monsterboard)
    new = movePackman(new)
    for i in range(4):
        for j in range(4):
            if org[i][j] == []:
                continue
            new[i][j].extend(org[i][j])
    monsterboard = new[:]
    for i in range(4):
        for j in range(4):
            for idx in range(len(deadboard[i][j])):
                deadboard[i][j][idx] += 1
                if deadboard[i][j][idx] == 0:
                    deadboard[i][j].pop(idx)

ans = 0
for i in range(4):
    for j in range(4):
        ans += len(monsterboard[i][j])

print(ans)
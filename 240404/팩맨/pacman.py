from collections import defaultdict

m,t = map(int,input().split())
r,c = map(int,input().split())
pi, pj = r-1, c-1
Monster = [list(map(int, input().split())) for _ in range(m)]
monsterboard = [[defaultdict(int) for i in range(4)] for _ in range(4)]

deadboard = [[[],[],[],[]] for _ in range(4)]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1] #↑, ↖, ←, ↙, ↓, ↘, →, ↗
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


for monster in Monster:
    r,c,d = monster
    monsterboard[r-1][c-1][d] += 1

def moveMonster(monsterboard):
    newboard = [[defaultdict(int) for i in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if len(monsterboard[i][j]) >0 :
                for md_, mcnt in monsterboard[i][j].items():
                    tcnt = 0
                    md = md_
                    while True:
                        ni, nj = i + dx[md], j + dy[md]
                        if ni<0 or ni >=4 or nj<0 or nj>=4 or len(deadboard[ni][nj]) > 0 or [ni,nj] == [pi,pj]:
                            md = (md+1)%9
                            if md == 0:
                                md += 1
                            tcnt +=1
                            if tcnt >= 8:
                                ni,nj,md = i,j, md_
                                break
                        else:
                            break
                    newboard[ni][nj][md] += mcnt
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
                    eatable[0] += sum([i for i in board[ni][nj].values()])
                    eatable[1].append([ni,nj])
                if skip:
                    continue
                if maxeat[0] < eatable[0]:
                    maxeat = eatable

    for mi,mj in maxeat[1]:
        if len(board[mi][mj]) == 0:
            continue
        board[mi][mj] = defaultdict(int)
        if -3 not in deadboard[mi][mj]:
            deadboard[mi][mj].append(-3)

    pi,pj = maxeat[1][2]

    return board

for turn in range(t):
    org, new = moveMonster(monsterboard)
    new = movePackman(new)

    for i in range(4):
        for j in range(4):
            for a,b in org[i][j].items():
                new[i][j][a] += b

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
        a = sum([i for i in monsterboard[i][j].values()])
        ans+=a
print(ans)
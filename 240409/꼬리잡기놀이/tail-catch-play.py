n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

teams = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            line = [[i,j]]
            end = False
            while True:
                x,y = line[-1]
                for d in range(4):
                    ni,nj = x+dx[d], y+dy[d]
                    if 0<=ni<n and 0<=nj<n:
                        if board[ni][nj] == 2 and [ni,nj] not in line:
                            line.append([ni,nj])
                        if board[x][y] == 2 and board[ni][nj] == 3:
                            line.append([ni,nj])
                            end = True
                if end:
                    break
            teams.append(line)

def moveTeam():
    for idx,team in enumerate(teams):
        si, sj = team[0]
        ei, ej = team.pop(-1)
        ei_, ej_ = team[-1]
        for d in range(4):
            si_, sj_ = si+dx[d], sj+dy[d]
            if 0<=si_<n and 0<=sj_<n and 3<=board[si_][sj_]<=4 and [si_,sj_] != team[1]:
                break
        team.insert(0, [si_,sj_])
        board[si][sj] = 2
        board[ei][ej] = 4
        board[ei_][ej_] = 3
        board[si_][sj_] = 1


def throwBall(round):
    global ans
    dir = (round//n) % 4
    line = round % n
    hit = False
    if dir == 0:
        for j in range(n):
            if 1<=board[line][j]<4:
                hx, hy = line, j
                for tidx, team in enumerate(teams):
                    if [hx,hy] in team:
                        pidx = team.index([hx,hy])
                        ans += (pidx+1)**2
                        teams[tidx] = team[::-1]
                        hit = True
                        break
                if hit:
                    break

    if dir == 1:
        for i in range(n-1, -1, -1):
            if 1<=board[i][line]<4:
                hx,hy = i, line
                for tidx, team in enumerate(teams):
                    if [hx,hy] in team:
                        pidx = team.index([hx,hy])
                        ans += (pidx+1)**2
                        teams[tidx] = team[::-1]
                        hit = True
                        break
                if hit:
                    break

    if dir == 2:
        for j in range(n-1,-1,-1):
            if 1<=board[n-1-line][j]<4:
                hx,hy = n-1-line, j
                for tidx, team in enumerate(teams):
                    if [hx,hy] in team:
                        pidx = team.index([hx,hy])
                        ans += (pidx+1)**2
                        teams[tidx] = team[::-1]
                        hit = True
                        break
                if hit:
                    break

    if dir == 3:
        for i in range(n):
            if 1<=board[i][n-1-line]<4:
                hx,hy = i, n-1-line
                for tidx, team in enumerate(teams):
                    if [hx,hy] in team:
                        pidx = team.index([hx,hy])
                        ans += (pidx+1)**2
                        teams[tidx] = team[::-1]
                        hit = True
                        break
                if hit:
                    break



ans = 0
for round in range(k):
    moveTeam()
    throwBall(round)
print(ans)
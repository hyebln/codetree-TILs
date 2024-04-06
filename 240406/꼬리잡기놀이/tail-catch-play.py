from collections import deque
n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]


def initState():
    global teams
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                team = [[i,j]]
                q = deque()
                q.append([i,j])
                visited[i][j] = 1
                while q:
                    x,y = q.popleft()
                    for d in range(4):
                        nx,ny= x+dx[d], y+dy[d]
                        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                            if board[nx][ny] == 2:
                                team.append([nx,ny])
                                visited[nx][ny] = 1
                                q.append([nx,ny])
                            if board[nx][ny] == 3:
                                team.append([nx,ny])
                teams.append(team)

def movePerson():
    for idx, team in enumerate(teams):
        si, sj = team[0]
        ei, ej = team.pop(-1)
        board[ei][ej] = 4
        for d in range(4):
            si_, sj_ = si+dx[d], sj+dy[d]
            if 0<=si_<n and 0<=sj_<n:
                if board[si_][sj_] == 4:
                    team = [[si_,sj_]] + team
                    board[si_][sj_] = 1
        board[si][sj] = 2
        board[team[-1][0]][team[-1][1]] = 3
        teams[idx] = team

def throwBall(rnd):
    global ans
    direction = (rnd//n)%4
    line = rnd % n
    loc = [-1,-1]
    if direction == 0:
        for j in range(n):
            if 1<= board[line][j]<=3:
                loc = [line,j]
                break
    elif direction == 1:
        for i in range(n-1, -1, -1):
            if 1<=board[i][line] <=3:
                loc = [i,line]
                break
    elif direction == 2:
        for j in range(n-1,-1,-1):
            if 1<=board[n-line-1][j] <=3:
                loc = [n-line-1, j]
                break
    elif direction == 3:
        for i in range(n):
            if 1<=board[i][n-1-line] <=3:
                loc = [i,n-1-line]
                break

    if loc == [-1,-1]:
        return

    for tidx, team in enumerate(teams):
        if loc in team:
            score = team.index(loc) +1
            ans += score**2
            teams[tidx] = team[::-1]
            changeheadtail(team)

def changeheadtail(t):
    si,sj = t[0]
    ei,ej = t[-1]
    board[si][sj], board[ei][ej] = board[ei][ej], board[si][sj]


teams = []
initState()
ans = 0
for rnd in range(k):
    movePerson()
    throwBall(rnd)
print(ans)
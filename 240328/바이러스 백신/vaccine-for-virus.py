import copy
from collections import deque

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
hospital = []
ans = 10e9

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            hospital.append([i,j])
            board[i][j] = 0
        if board[i][j] == 1:
            board[i][j] = -1

def dfs(hospital_list, pick_list, idx):
    if idx == len(hospital_list):
        if len(pick_list) == m:
            hospital_sel.append(pick_list[:])
        return
    pick_list.append(hospital_list[idx])
    dfs(hospital_list, pick_list, idx+1)
    pick_list.pop()
    dfs(hospital_list, pick_list, idx+1)

def setHospital(hos):
    global ans, fail

    q = deque()
    newboard = copy.deepcopy(board)
    for i, j in hos:
        newboard[i][j] = 1
        q.append([i,j])

    while q:
        x,y = q.popleft()
        dist = newboard[x][y]
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<n and 0<=ny<n and newboard[nx][ny] ==0:
                newboard[nx][ny] = dist + 1
                q.append([nx,ny])

    for i,j in hospital:
        board[i][j] = -3

    maxd = 0
    for i in range(n):
        for j in range(n):
            if newboard[i][j] == 0:
                fail = False
                return
            if newboard[i][j] > 0:
                if maxd < newboard[i][j]:
                    if [i,j] in hospital:
                        maxd = newboard[i][j] -1
                        continue
                    maxd = newboard[i][j]

    if maxd >0:
        maxd -= 1
    fail = True
    ans = min(ans, maxd)

hospital_sel = []
fail= True
dfs(hospital, [], 0)

for sel in hospital_sel:
    setHospital(sel)

if fail:
    print(ans)
else:
    print(-1)
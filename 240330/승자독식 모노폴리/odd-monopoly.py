import copy

n,m,k = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
first_d = list(map(int,input().split()))
direction_priority = [[] for _ in range(m)]
for idx in range(m):
    for dir in range(4):
        a = list(map(int,input().split()))
        direction_priority[idx].append([i-1 for i in a])

player = [0]*m
dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            idx = board[i][j] -1
            board[i][j] = [idx, k]
            player[idx] = [i,j,first_d[idx]-1]


def movePlayer():
    newboard = [[[]for _ in range(n)] for i in range(n)]

    for idx in range(4):
        if player[idx] == []:
            continue
        pi,pj,pd = player[idx]
        emptyboard = []
        myboard = []
        for d in direction_priority[idx][pd]:
            ni = pi+dx[d]
            nj = pj+dy[d]
            if 0<=ni<n and 0<=nj<n:
                if board[ni][nj] == 0:
                    emptyboard= [ni,nj,d]
                    break
                elif board[ni][nj][0] == idx:
                    myboard.append([ni,nj,d])

        if emptyboard ==[] and myboard != []:
            emptyboard = myboard[0]


        ti, tj, td = emptyboard
        newboard[ti][tj].append([idx, k+1])
        player[idx] = [ti, tj, td]

    for i in range(n):
        for j in range(n):
            if newboard[i][j] ==[]:
                continue
            idx, life = newboard[i][j][0][0], newboard[i][j][0][1]
            board[i][j] = [idx, life]
            if len(newboard[i][j]) > 1:
                for re in range(1, len(newboard[i][j])):
                    ridx,rlife = newboard[i][j][re]
                    player[ridx] = []
def removeOne():
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                board[i][j][1] -=1
                if board[i][j][1] == 0:
                    board[i][j] = 0
turn = 0
while True:
    turn += 1
    if turn >=1000:
        print(-1)
        break
    movePlayer()
    removeOne()
    if player[0] != [] and player.count([]) == m-1:
        print(turn)
        break
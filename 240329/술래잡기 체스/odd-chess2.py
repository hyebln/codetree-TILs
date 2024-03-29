import copy

board = [[0]*4 for _ in range(4)]

for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        p,d = info[j*2], info[(2*j)+1]
        board[i][j] = [p-1, d-1]


dx = [-1, -1, 0, 1, 1, 1, 0, -1]# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def moveThief():
    for idx in range(16):
        move = False
        for i in range(4):
            for j in range(4):
                if board[i][j] == -1 or board[i][j] == []:
                    continue
                if board[i][j][0] == idx:
                    d = board[i][j][1]
                    turn = 0
                    while True:
                        ni = i + dx[d]
                        nj = j + dy[d]
                        if 0<=ni<4 and 0<=nj<4 and board[ni][nj] != -1:
                            break
                        d = (d+1)%8
                        turn += 1
                        if turn ==8:
                            break
                    if turn == 8:
                        continue
                    changethief = board[ni][nj][:]
                    board[ni][nj] = [idx,d]
                    board[i][j] = changethief
                    move = True
                if move:
                    break
            if move:
                break

def done(ci, cj, cd):
    done = True
    for dist in range(1, 4):
        ti = ci+dx[cd]*dist
        tj = ci+dy[cd]*dist
        if 0<=ti<4 and 0<=tj<4 and board[ti][tj] != [] and board[ti][tj] != -1 :
            done = False
    return done


def moveCatcher(c, score):
    global maxans
    ci, cj, cd = c
    if done(ci, cj, cd):
        maxans = max(maxans, score)
        return
    for dist in range(1, 4):
        ti = ci+dx[cd]*dist
        tj = cj+dy[cd]*dist
        if 0<=ti<4 and 0<=tj<4:
            if board[ti][tj] in [[], -1]:
                continue
            targetidx, targetdir = board[ti][tj]
            newboard = copy.deepcopy(board)
            board[ti][tj], board[ci][cj] = -1, []
            moveThief()
            moveCatcher([ti, tj, targetdir], score+targetidx+1)
            for i in range(4):
                for j in range(4):
                    board[i][j] = newboard[i][j]



catcher = [0,0, board[0][0][1]]
ans = board[0][0][0]+1
board[0][0] = -1

maxans = 0
moveThief()
moveCatcher(catcher, ans)
print(maxans)
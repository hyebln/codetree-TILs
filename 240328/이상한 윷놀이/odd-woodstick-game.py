n,k = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
horse = [list(map(int, input().split())) for _ in range(k)]
horseboard = [[[]for i in range(n)] for _ in range(n)]
dx = [0, 0, -1, 1] #우좌 상하
dy = [1, -1, 0, 0]

for i in range(k):
    x,y,d = horse[i]
    horseboard[x-1][y-1].append(i)
    horse[i] = [x-1, y-1, d-1]

def change_dir(org_d):
    if org_d%2 ==0:
        org_d += 1
    else:
        org_d -= 1
    return org_d

def moveWhite(idx):
    i, j, d = horse[idx]
    listt = horseboard[i][j]
    order = listt.index(idx)
    horseboard[i][j] = listt[:order]
    for ord in listt[order:]:
        horse[ord][0], horse[ord][1] = ni, nj
        horseboard[ni][nj].append(ord)

def moveRed(idx):
    i, j, d = horse[idx]
    listt = horseboard[i][j]
    order = listt.index(idx)
    horseboard[i][j] = listt[:order]
    for ord in listt[order:]:
        horse[ord][0], horse[ord][1] = ni, nj
    horseboard[ni][nj].extend(listt[order:][::-1])


def moveBlue(idx):
    i, j, d = horse[idx]
    d = change_dir(d)
    ni = i + dx[d]
    nj = j + dy[d]
    horse[idx] = [i,j,d]
    listt = horseboard[i][j]
    order = listt.index(idx)
    horseboard[i][j] = listt[:order]
    if 0<=ni<n and 0<=nj<n and board[ni][nj] ==0: #흰색
        for ord in listt[order:]:
            horse[ord][0], horse[ord][1] = ni, nj
            horseboard[ni][nj].append(ord)

    elif 0<=ni<n and 0<=nj<n and board[ni][nj] ==1: #빨간색
        for ord in listt[order:]:
            horse[ord][0], horse[ord][1] = ni, nj
        horseboard[ni][nj].extend(listt[order:][::-1])

    else: #파란색
        for ord in listt[order:]:
            horseboard[i][j].append(ord)


turn =0
stack4 = False
while True:
    if stack4 or turn > 100:
        break
    for idx in range(k):
        i,j,d = horse[idx]
        ni = i + dx[d]
        nj = j + dy[d]
        if 0<=ni<n and 0<=nj<n and board[ni][nj] ==0:
            #흰색
            moveWhite(idx)

        elif 0<=ni<n and 0<=nj<n and board[ni][nj] ==1:
            #빨강
            moveRed(idx)
        else:
            #파랑&막다른길
            moveBlue(idx)

        for i in range(n):
            for j in range(n):
                if len(horseboard[i][j]) >=4:
                    stack4 = True
                    break
            if stack4:
                break
                
    turn+=1
print(turn)
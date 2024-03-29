import copy

k = int(input())
blocks = [list(map(int, input().split())) for _ in range(k)]

redboard = [[0]*4 for i in range(6)]
yellowboard = [[0]*4 for i in range(6)]


def fillYellow(t,x,y):
    endline= 5
    if t in [1, 3]:
        for i in range(6):
            if yellowboard[i][y] == 1:
                endline = i-1
                break

    if t == 2:
        for i in range(6):
            if yellowboard[i][y] == 1 or yellowboard[i][y+1] == 1:
                endline = i-1
                break

    yellowboard[endline][y] = 1
    if t == 3:
        yellowboard[endline-1][y] = 1
    elif t == 2:
        yellowboard[endline][y+1] = 1


def fillRed(t,x,y):
    endline= 5
    y_ = abs(x-3)
    if t in [1, 2]:
        for i in range(6):
            if redboard[i][y_] == 1:
                endline = i-1
                break
    if t == 3:
        for i in range(6):
            if redboard[i][y_] == 1 or redboard[i][y_-1] == 1:
                endline = i-1
                break
    redboard[endline][y_] = 1
    if t == 2:
        redboard[endline-1][y_] = 1
    elif t == 3:
        redboard[endline][y_-1] = 1

def checkScore():
    global ans, redboard, yellowboard
    scoreyel = []
    scorered = []
    for i in range(6):
        if sum(yellowboard[i]) == 4:
            scoreyel.append(i)
        if sum(redboard[i]) == 4:
            scorered.append(i)

    ans += len(scorered)+len(scoreyel)
    for idx in scorered[::-1]:
        redboard.pop(idx)
    redboard = [[0]*4 for _ in range(len(scorered))]+redboard

    for idx in scoreyel[::-1]:
        yellowboard.pop(idx)
    yellowboard = [[0]*4 for _ in range(len(scoreyel))]+yellowboard


def delUpper():
    deletered = 0
    deleteyel = 0
    newredboard = copy.deepcopy(redboard)
    newyelboard = copy.deepcopy(yellowboard)
    for i in range(2):
        if sum(redboard[i]) > 0:
            deletered += 1
        if sum(yellowboard[i]) > 0:
            deleteyel += 1


    if deletered>0:
        newredboard = [[0]*4 for _ in range(deletered)]+ redboard[:-deletered]

    if deleteyel > 0:
        newyelboard = [[0] * 4 for _ in range(deleteyel)] + yellowboard[:-deleteyel]

    return newredboard, newyelboard


ans = 0
for b in blocks:
    t,x,y = b
    fillYellow(t,x,y)
    fillRed(t,x,y)
    checkScore()
    redboard, yellowboard = delUpper()


print(ans)
sumboard = 0
for i in range(6):
    sumboard += sum(redboard[i]) + sum(yellowboard[i])
print(sumboard)
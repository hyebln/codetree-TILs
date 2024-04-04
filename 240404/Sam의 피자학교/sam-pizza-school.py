import copy

n,k = map(int,input().split())
flour = list(map(int,input().split()))

def addFlour():
    minF = min(flour)
    for idx in range(n):
        if flour[idx] == minF:
            flour[idx] += 1

def rollFlour():
    board = [[flour[0]], flour[1:]]
    while True:
        l = len(board[0])
        if len(board) > len(board[-1]) - l:
            break
        newboard = [board[-1][l:]]
        splited = []
        for i in range(len(board)):
            splitt = []
            for j in range(l):
                splitt.append(board[i][j])
            splited.append(splitt)
        turnsplited = list(map(list, zip(*splited[::-1])))
        turnsplited.extend(newboard)
        board=turnsplited[:]
    return board

def pushFlour():
    dx = [1, 0]
    dy = [0, 1]
    origin = copy.deepcopy(flour)
    for i in range(len(flour)):
        for j in range(len(flour[i])):
            a = flour[i][j]
            for d in range(2):
                ni, nj = i+dx[d], j+dy[d]
                if 0<=ni<len(flour) and 0<=nj<len(flour[ni]):
                    b = flour[ni][nj]
                    val = abs(a-b) // 5
                    if a > b:
                        origin[i][j] -= val
                        origin[ni][nj] += val
                    elif a < b:
                        origin[i][j] += val
                        origin[ni][nj] -= val

    newflour = []
    for j in range(len(origin[-1])):
        for i in range(len(origin), -1, -1):
            if 0 <= i < len(origin) and 0 <= j < len(origin[i]):
                newflour.append(origin[i][j])
    return newflour

def foldFlour():
    lenf = len(flour)
    newflour = [flour[:lenf//2][::-1]] + [flour[lenf//2::]]
    finalf = []
    for i in [1,0]:
        listf = newflour[i][:lenf//4]
        finalf.append(listf[::-1])
    newflour[i][lenf//4:]
    for i in range(2):
        finalf.append([a for a in newflour[i][lenf//4:]])

    return finalf



turn = 0
while True:
    maxf = max(flour)
    minf = min(flour)
    if maxf - minf <= k:
        print(turn)
        break
    addFlour()
    flour = rollFlour()
    flour = pushFlour()
    flour = foldFlour()
    flour = pushFlour()
    turn += 1
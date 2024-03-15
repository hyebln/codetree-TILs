from collections import defaultdict
r,c,k = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(3)]


def sortBoard(n,m):
    newBoard = []
    maxlen =0
    for i in range(n):
        cntdict = defaultdict(int)
        for num in board[i]:
            if num ==0:
                continue
            cntdict[num] += 1
        maxlen = max(maxlen, len(cntdict)*2)
        cntlist = [list(i) for i in cntdict.items()]
        cntlist.sort(key=lambda x:[x[1], x[0]])
        newBoard.append(sum(cntlist, []))
    for i in range(n):
        if len(newBoard[i]) < maxlen:
            newBoard[i] += [0]* (maxlen-len(newBoard[i]))

    return newBoard

def sortBoard_(n,m):
    newBoard = []
    maxlen =0
    for j in range(m):
        cntdict = defaultdict(int)
        for i in range(n):
            num = board[i][j]
            if num ==0:
                continue
            cntdict[num] += 1
        maxlen = max(maxlen, len(cntdict)*2)
        cntlist = [list(i) for i in cntdict.items()]
        cntlist.sort(key=lambda x:[x[1], x[0]])
        newBoard.append(sum(cntlist, []))

    for i in range(m):
        if len(newBoard[i]) < maxlen:
            newBoard[i] += [0]* (maxlen-len(newBoard[i]))
    newBoard = [list(x) for x in zip(*newBoard)]

    return newBoard



time = 0
while True:
    if time > 100:
        time = -1
        break
    if len(board) >= r and len(board[0])>=c:
        if board[r-1][c-1] == k:
            break


    a = len(board)
    b = len(board[0])
    if a >= b:
        board = sortBoard(a,b)
    else:
        board = sortBoard_(a,b)

    if len(board) > 100:
        board = board[:100]
    elif len(board[0]) > 100:
        for i in range(len(board)):
            board[i] = board[i][:100]

    time += 1
print(time)
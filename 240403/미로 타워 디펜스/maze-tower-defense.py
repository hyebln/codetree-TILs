n,m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
player = [list(map(int, input().split())) for _ in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
px, py = n//2, n//2

def attackM(atk):
    global ans
    d, p = atk
    for dist in range(1,p+1):
        x,y = px+dx[d]*dist, py+dy[d]*dist
        ans += board[x][y]
        board[x][y] = 0

def moveM():
    global ans
    Mlist = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    si, sj, sd = px,py,0
    dist = 1
    stop = True
    while stop:
        for _ in range(2):
            for di in range(dist):
                si += dx[sd]
                sj += dy[sd]
                if board[si][sj] > 0 and 0<=si<n and 0<=sj<n:
                    Mlist.append(board[si][sj])
                if [si,sj] == [0,0]:
                    stop = False
            if not stop:
                break
            sd = (sd+1)%4
        dist += 1

    while True:
        deleteidx = []
        cnt = 1
        for idx in range(1, len(Mlist)):
            if Mlist[idx] == Mlist[idx-1]:
                cnt += 1
            else:
                if cnt >= 4:
                    deleteidx.extend([i for i in range(idx-cnt, idx)])
                cnt = 1

        if cnt >= 4:
            deleteidx.extend([i for i in range(idx-cnt, idx)])
        if deleteidx == []:
            break
        for idx in deleteidx[::-1]:
            a = Mlist.pop(idx)
            ans += a

    result = []
    numlist= [-1,-1]
    while Mlist:
        a = Mlist.pop(0)
        if a == numlist[0]:
            numlist[1] += 1
        else:
            result.extend(numlist[::-1])
            numlist = [a, 1]
    result.extend(numlist[::-1])
    return result[2:]


def insertM(listM):
    board = [[0]*n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    si, sj, sd = px,py,0
    dist = 1
    stop = True
    while stop:
        for _ in range(2):
            for di in range(dist):
                si += dx[sd]
                sj += dy[sd]
                if 0<=si<n and 0<=sj<n:
                    if listM == []:
                        continue
                    a = listM.pop(0)
                    board[si][sj] = a
                    if listM == []:
                        stop = False
                if [si,sj] == [0,0]:
                    stop = False
            if not stop:
                break
            sd = (sd+1)%4
        dist += 1
    return board

ans = 0
for p in player:
    attackM(p)
    newM = moveM()
    board = insertM(newM)


print(ans)
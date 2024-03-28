n,m,q= map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rotate_list= [list(map(int,input().split())) for _ in range(q)]


def boardRotate(i,d,k):
    turnlist = board[i]
    if d == 0: # 시계
        turned = turnlist[-k:]+turnlist[:-k]
    if d == 1: # 반시계
        turned = turnlist[k:]+turnlist[:k]
    board[i] = turned[:]

def checkBoard():
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visited = [[0]*m for _ in range(n)]
    deletenum = False
    for i in range(0,n):
        for j in range(0,m):
            if board[i][j] ==0:
                continue
            for d in range(4):
                ni = (i+dx[d])%n
                nj = (j+dy[d])%m
                if i in [0, n-1]:
                    ni = i + dx[d]
                    if ni<0 or ni>=n:
                        continue
                if board[ni][nj] == board[i][j]:

                    deletenum = True
                    visited[i][j] = 1
                    visited[ni][nj] = 1

    if deletenum:
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    board[i][j] = 0
    else:
        sum = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] >0:
                    cnt += 1
                    sum += board[i][j]
        avg = sum // cnt
        for i in range(n):
            for j in range(m):
                if board[i][j] ==0:
                    continue
                if board[i][j] > avg:
                    board[i][j] -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1


def answer():
    ans=0
    for i in range(n):
        ans += sum(board[i])
    print(ans)
    
for x,d,k in rotate_list:
    boardRotate(x-1,d,k)
    checkBoard()
answer()
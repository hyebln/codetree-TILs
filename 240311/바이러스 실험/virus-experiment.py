from collections import deque

n,m,k = map(int,input().split())
adds = [list(map(int, input().split())) for _ in range(n)]
virus = [[] for _ in range(n)]
dead = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        virus[i].append(deque())
        dead[i].append([])
for _ in range(m):
    i,j,age = map(int, input().split())
    virus[i-1][j-1].append(age)

board = [[5]*n for _ in range(n)]
def eating():
    newboard = [[0]*n for _ in range(n)]
    for vi in range(n):
        for vj in range(n):
            len_ = len(virus[vi][vj])

            for k in range(len_):
                age = virus[vi][vj][k]
                if board[vi][vj] >= age:
                    board[vi][vj] -= age
                    virus[vi][vj][k] += 1
                else:
                    for _ in range(k, len_):
                        dead[vi][vj].append(virus[vi][vj].pop())
                    break

    for i in range(n):
        for j in range(n):
            board[i][j] += newboard[i][j]
            while dead[i][j]:
                board[i][j] += dead[i][j].pop() // 2

def seperatevirus():
    dx = [-1,-1,-1,0,1,1,1,0]
    dy = [-1,0,1,1,1,0,-1,-1]
    for i in range(n):
        for j in range(n):
            for k in range(len(virus[i][j])):
                if virus[i][j][k] %5 == 0:
                    for d in range(8):
                        ni = i + dx[d]
                        nj = j + dy[d]
                        if 0<=ni<n and 0<=nj<n:
                            virus[ni][nj].appendleft(1)

def addnourish():
    for i in range(n):
        for j in range(n):
            board[i][j] += adds[i][j]

for cycle in range(k):
    eating()
    seperatevirus()
    addnourish()


cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(virus[i][j])
print(cnt)
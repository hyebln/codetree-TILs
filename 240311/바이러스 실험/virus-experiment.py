import copy

n,m,k = map(int,input().split())
adds = [list(map(int, input().split())) for _ in range(n)]
virus = []
for _ in range(m):
    i,j,age = map(int, input().split())
    virus.append([i-1, j-1, age])

board = [[5]*n for _ in range(n)]
def eating():
    virus.sort(key=lambda x:x[2])
    newboard = [[0]*n for _ in range(n)]
    for idx, [vi, vj, age] in enumerate(virus):
        if board[vi][vj] >= age:
            board[vi][vj] -= age
            virus[idx] = [vi,vj, age+1]
        else:
            dead = age// 2
            virus[idx] = []
            newboard[vi][vj] += dead

    for i in range(n):
        for j in range(n):
            board[i][j] += newboard[i][j]

    for idx in range(len(virus)-1, -1, -1):
        if virus[idx] == []:
            virus.pop(idx)
def seperatevirus():
    dx = [-1,-1,-1,0,1,1,1,0]
    dy = [-1,0,1,1,1,0,-1,-1]
    newvirus = []
    for idx, [vi, vj, age] in enumerate(virus):
        if age % 5 == 0:
            for d in range(8):
                ni = vi + dx[d]
                nj = vj + dy[d]
                if 0<=ni<n and 0<=nj<n:
                    newvirus.append([ni,nj,1])
    virus.extend(newvirus)


def addnourish():
    for i in range(n):
        for j in range(n):
            board[i][j] += adds[i][j]


for cycle in range(k):
    eating()
    seperatevirus()
    addnourish()
print(len(virus))
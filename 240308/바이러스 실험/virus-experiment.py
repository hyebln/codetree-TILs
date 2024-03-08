n,m,k = map(int,input().split())
adds = [list(map(int, input().split())) for _ in range(n)]
virus = [list(map(int, input().split())) for _ in range(m)]

board = [[5]*n for _ in range(n)]
def eating():
    for idx, [vi, vj, age] in enumerate(virus):
        vi -= 1
        vj -= 1
        if board[vi][vj] >= age:
            board[vi][vj] -= age
            virus[idx] = [vi+1,vj+1, age+1]
        else:
            virus[idx] = []
            board[vi][vj] += age//2
    for idx in range(len(virus)-1, -1, -1):
        if virus[idx] == []:
            virus.pop(idx)
def seperatevirus():
    dx = [-1,-1,-1,0,1,1,1,0]
    dy = [-1,0,1,1,1,0,-1,-1]
    for idx, [vi, vj, age] in enumerate(virus):
        vi -= 1
        vj -= 1
        if age % 5 == 0:
            for d in range(8):
                ni = vi + dx[d]
                nj = vj + dy[d]
                if 0<=ni<n and 0<=nj<n:
                    virus.append([ni+1,nj+1,1])



def addnourish():
    for i in range(n):
        for j in range(n):
            board[i][j] += adds[i][j]
            continue

for cycle in range(k):
    eating()
    seperatevirus()
    addnourish()
print(len(virus))
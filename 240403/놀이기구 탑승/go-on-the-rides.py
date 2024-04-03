from collections import defaultdict

n=int(input())
students =[list(map(int, input().split())) for _ in range(n*n)]
board = [[0]*n for _ in range(n)]
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def findLoc(student):
    target = [0,0,-1,-1] #i,j,like, empty
    idx, a,b,c,d = student
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                continue
            empty, likes = 0,0
            for dir in range(4):
                ni, nj = i+dx[dir], j+dy[dir]
                if 0<=ni<n and 0<=nj<n:
                    if board[ni][nj] == 0:
                        empty += 1
                    if board[ni][nj] in [a,b,c,d]:
                        likes += 1
            if (target[2], target[3], -target[0], -target[1]) < (likes, empty, -i, -j):
                target = [i, j,likes, empty]
    x,y, = target[0], target[1]
    board[x][y] = idx

def calScore():
    ans = 0
    for i in range(n):
        for j in range(n):
            idx = board[i][j]
            score = 0
            for dir in range(4):
                ni, nj = i+dx[dir], j+dy[dir]
                if 0<=ni<n and 0<=nj<n:
                    if board[ni][nj] in studentlist[idx]:
                        score += 1
            if score >0:
                ans += 10**(score-1)
    print(ans)
    
studentlist = defaultdict(list)
for st in students:
    studentlist[st[0]] = st[1:]
    findLoc(st)
calScore()
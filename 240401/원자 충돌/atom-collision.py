n,m,k=map(int,input().split())
atoms = [list(map(int,input().split())) for _ in range(m)]
board = [[[] for i in range(n)] for _ in range(n)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for at in atoms:
    x,y,m,s,d = at
    board[x-1][y-1].append([m,s,d])

def moveAtoms():
    newboard = [[[] for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for cnt in range(len(board[i][j])):
                    m,s,d = board[i][j][cnt]
                    ni, nj =(i + dx[d]*s)%n, (j + dy[d]*s)%n
                    newboard[ni][nj].append([m,s,d])

    for i in range(n):
        for j in range(n):
            if len(newboard[i][j]) > 1:
                sumlist = newboard[i][j]
                sum_m, sum_s = 0, 0
                dirs = []
                for idx in range(len(sumlist)):
                    sum_m += sumlist[idx][0]
                    sum_s += sumlist[idx][1]
                    dirs.append(sumlist[idx][2]%2)
                avg_m = sum_m // 5
                avg_s = sum_s // len(sumlist)
                newboard[i][j] = []
                if avg_m == 0:
                    continue
                if sum(dirs) ==0 or sum(dirs) == len(dirs):
                    for newd in [0,2,4,6]:
                        newboard[i][j].append([avg_m, avg_s, newd])
                else:
                    for newd in [1,3,5,7]:
                        newboard[i][j].append([avg_m, avg_s, newd])

    return newboard

for i in range(k):
    board = moveAtoms()

ans = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            for cnt in range(len(board[i][j])):
                ans += board[i][j][cnt][0]

print(ans)
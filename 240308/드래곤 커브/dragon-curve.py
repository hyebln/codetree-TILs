n = int(input())
dragonC = [list(map(int,input().split())) for _ in range(n)]
board = [[0]*101 for _ in range(101)]
dx = [0, -1, 0, 1] #우 상 좌 하
dy = [1, 0, -1, 0]

def drawcurve(x,y,d,g):
    moveroute= [d]
    for step in range(g):
        for r in moveroute[::-1]:
            moveroute.append((r+1)%4)
    board[x][y] = 1
    for route in moveroute:
        x += dx[route]
        y += dy[route]
        board[x][y] = 1

for idx,dcurve in enumerate(dragonC):
    x,y,d,g = dcurve
    drawcurve(x,y,d,g)

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
            ans += 1


print(ans)
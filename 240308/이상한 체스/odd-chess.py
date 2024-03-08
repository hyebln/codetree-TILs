import copy

n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0] #북, 동, 남, 서
dy = [0, 1, 0, -1]
direction = [[],
             [[0],[1],[2],[3]],
             [[0,2],[1,3]],
             [[0,1],[1,2],[2,3],[3,0]],
             [[3,0,1],[0,1,2],[1,2,3],[2,3,0]],
             [[0,1,2,3]]]

def fillboard(cx,cy,direction, tmp):
    for dir in direction:
        nx, ny = cx, cy
        while True:
            nx += dx[dir]
            ny += dy[dir]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny] != 6:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
            else:
                break

def dfs(board, cnt):
    global ans

    cboard = copy.deepcopy(board)
    if cnt == totalcnt:
        fillcnt = 0
        for i in cboard:
            fillcnt += i.count(0)
        ans = min(fillcnt, ans)
        return
    x,y,horse = horses[cnt]
    for i in direction[horse]:
        fillboard(x,y,i,cboard)
        dfs(cboard, cnt+1)
        cboard = copy.deepcopy(board)

ans = 10e9
horses = []
totalcnt = 0
for i in range(n):
    for j in range(m):
        if 0<board[i][j]<6:
            horses.append([i,j,board[i][j]])
            totalcnt += 1
dfs(board, 0)

print(ans)
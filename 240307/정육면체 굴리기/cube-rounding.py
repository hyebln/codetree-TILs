n,m,x,y,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions = list(map(int, input().split()))

dice = [[0, 0], [0, 0], [0, 0]]
loc = [0, 0]
dx = [0, 0, 0, -1, 1] # 동,서,북,남
dy = [0, 1, -1, 0, 0]
def move(dir, dice, loc):
    cx, cy = loc
    nx, ny = cx+dx[dir], cy+dy[dir]
    if 0<=nx<n and 0<=ny<m:
        if dir == 1:
            dice = [dice[1], dice[0][::-1], dice[2]]

        elif dir == 2:
            dice = [dice[1][::-1], dice[0], dice[2]]

        elif dir == 3:
            dice = [dice[2], dice[1], dice[0][::-1]]

        elif dir == 4:
            dice = [dice[2][::-1], dice[1], dice[0]]

        if board[nx][ny] == 0:
            board[nx][ny] = dice[0][1]
        else:
            dice[0][1] = board[nx][ny]
            board[nx][ny] = 0

        print(dice[0][0])
    else:
        nx, ny = loc
    return dice, [nx,ny]
for dir in directions:
    dice, loc = move(dir, dice, loc)
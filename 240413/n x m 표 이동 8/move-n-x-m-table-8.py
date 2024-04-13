k = int(input())
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

def move(x,y, cnt1, cnt2):
    global minmove
    dx1 = [-1,-2,-2,-1,1,2,2,1]
    dy1 = [-2,-1,1,2,2,1,-1,-2]

    dx2 = [-1,0,1,0]
    dy2 = [0,1,0,-1]
    if [x,y] == [n-1,m-1]:
        minmove = min(len(cnt1+cnt2), minmove)


    if len(cnt1) <k:
        for d in range(8):
            nx = x+dx1[d]
            ny = y+dy1[d]
            if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            cnt1.append([nx,ny])
            move(nx,ny, cnt1, cnt2)
            visited[nx][ny] = 0
            cnt1.pop(-1)

        for d in range(4):
            nx = x+dx2[d]
            ny = y+dy2[d]
            if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            cnt2.append([nx,ny])
            move(nx,ny, cnt1, cnt2)
            visited[nx][ny] = 0
            cnt2.pop(-1)
    else:
        for d in range(4):
            nx = x+dx2[d]
            ny = x+dy2[d]
            if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            cnt2.append([nx,ny])
            move(nx,ny, cnt1, cnt2)
            visited[nx][ny] = 0
            cnt2.pop(-1)


ans = 0
minmove = 10e9
visited = [[0]*m for _ in range(n)]
move(0,0,[],[])
print(minmove)
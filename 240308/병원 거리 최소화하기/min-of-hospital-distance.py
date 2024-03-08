from  collections import deque

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

hospital = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            hospital.append([i,j])

visited = [0]*len(hospital)


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def caldistance(selected):
    global ans
    dist = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                q = deque()
                q.append([i,j])
                visited = [[0]*n for _ in range(n)]
                visited[i][j] = 1
                while q:
                    cx, cy = q.popleft()
                    if [cx,cy] in selected:
                        dist += abs(cx-i) + abs(cy-j)
                        break
                    for d in range(4):
                        nx = cx + dx[d]
                        ny = cy + dy[d]
                        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                            q.append([nx,ny])
    ans = min(ans, dist)
def select(arr, n):
    if n == m:
        caldistance(arr)
        return
    for i in range(len(hospital)):
        if not visited[i]:
            visited[i] = 1
            arr.append(hospital[i])
            select(arr, n+1)
            arr.pop()
            visited[i] = 0
ans = 10e9
select([], 0)
print(ans)
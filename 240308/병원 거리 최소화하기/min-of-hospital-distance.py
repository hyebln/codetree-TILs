from  collections import deque

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

hospital = []
person = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            hospital.append([i,j])
        elif board[i][j] == 1:
            person.append([i,j])


def caldistance(selected):
    global ans
    dist = 0
    for i,j in person:
        minds = 10e9
        for hp in selected:
            ds = abs(i-hp[0]) + abs(j-hp[1])
            minds = min(ds, minds)
        dist += minds
    ans = min(ans, dist)


def select(arr, n):
    if n == m:
        caldistance(arr)
        return
    for i in range(n,len(hospital)):
        if not visited[i]:
            visited[i] = 1
            arr.append(hospital[i])
            select(arr, n+1)
            arr.pop()
            visited[i] = 0

ans = 10e9
visited = [0]*len(hospital)
select([], 0)
print(ans)
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

def select(si, num):
    if num == m:
        caldistance(selectedarr)
        return

    for i in range(si, len(hospital)):
        if not visited[i]:
            selectedarr.append(hospital[i])
            visited[i] = 1
            select(i+1, num+1)
            visited[i] = 0
            selectedarr.pop()

ans = 10e9
visited = [0]*len(hospital)
selectedarr = []
select(0, 0)
print(ans)
from collections import defaultdict

n,L,R = map(int, input().split())
eggs = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def seperateEgg():
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1
    group = 1
    groupdic = defaultdict(list)
    for i in range(n):
        for j in range(n):
            num = eggs[i][j]
            if visited[i][j] == 0:
                group += 1
                visited[i][j] = group
            else:
                group = visited[i][j]

            for d in range(2):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0<=ni<n and 0<=nj<n:
                    besides = eggs[ni][nj]
                    if L<=abs(besides-num)<=R:
                        visited[ni][nj] = group
            groupdic[group].append(num)

    if visited[-1][-1] == n**2:
        return []
    for idx, egg in groupdic.items():
        avg = sum(egg) // len(egg)
        groupdic[idx] = avg

    for i in range(n):
        for j in range(n):
            id = visited[i][j]
            visited[i][j] = groupdic[id]

    return visited

ans = 0
while True:
    eggs = seperateEgg()
    if eggs == []:
        break
    ans += 1
print(ans)
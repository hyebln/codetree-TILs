from collections import defaultdict, deque

n,L,R = map(int, input().split())
eggs = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def seperateEgg():
    visited = [[0]*n for _ in range(n)]
    groupidx = 1
    groupdic = defaultdict(list)
    q = deque()
    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0:
                continue
            q.append([i,j])
            visited[i][j] = groupidx
            while q:
                ci, cj = q.popleft()
                num = eggs[ci][cj]
                for d in range(4):
                    ni = ci + dx[d]
                    nj = cj + dy[d]
                    if 0<=ni<n and 0<=nj<n and visited[ni][nj]==0:
                        besides = eggs[ni][nj]
                        if L<=abs(besides-num)<=R:
                            q.append([ni, nj])
                            visited[ni][nj] = groupidx
                groupdic[groupidx].append(num)
            groupidx += 1

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
import copy

n,m,k=map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
people = [[]]
for _ in range(m):
    x,y = map(int,input().split())
    people.append([x-1,y-1])
exit = list(map(int,input().split()))
exit[0] -= 1
exit[1] -= 1
move = [0]*(m+1)

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def movePeople():
    ei, ej = exit
    for idx in range(m+1):
        if people[idx]:
            i,j = people[idx]
            dist = abs(i-ei)+abs(j-ej)
            next = [-1, -1, 5]
            for d in range(4):
                ni,nj = i+dx[d], j+dy[d]
                if 0<=ni<n and 0<=nj<n and not board[ni][nj]:
                    ndist = abs(ni-ei)+abs(nj-ej)
                    if (dist, next[2]) > (ndist, d):
                        dist = ndist
                        next = [ni,nj,d]
            if next[0] == -1:
                people[idx] = [i,j]
            elif [next[0], next[1]] == exit:
                move[idx] += 1
                people[idx] = []
            else:
                people[idx] = next[:2]
                move[idx] += 1
                
def rotateBoard():
    ei, ej = exit
    orgboard = copy.deepcopy(board)
    orgboard[ei][ej] = -1
    for idx in range(m+1):
        if people[idx]:
            i,j = people[idx]
            orgboard[i][j] = -10*idx
            
    dist = 2
    select = [10e9,10e9,10e9]
    while dist <=n:
        for i in range(0,n-dist+1):
            for j in range(0,n-dist+1):
                exitcnt = 0
                personcnt = 0
                for dx in range(dist):
                    for dy in range(dist):
                        if orgboard[i+dx][j+dy] == -1:
                            exitcnt += 1
                        if orgboard[i+dx][j+dy] < -1:
                            personcnt += 1
                if exitcnt and personcnt:
                    if (select[2], select[0], select[1]) > (dist,i,j):
                        select = [i,j,dist]
        dist += 1

    si, sj, sdist = select
    small = []
    for i in range(si,si+sdist):
        line = orgboard[i]
        small.append(line[sj:sj+sdist])
    small_ = list(map(list, zip(*small[::-1])))
    for i in range(sdist):
        for j in range(sdist):
            if small_[i][j] <= 0:
                orgboard[i+si][j+sj] = small_[i][j]
            else:
                orgboard[i+si][j+sj] = small_[i][j] -1

    for i in range(n):
        for j in range(n):
            if orgboard[i][j] < -1:
                idx = abs(orgboard[i][j] // 10)
                people[idx] = [i,j]
                orgboard[i][j] = 0
            if orgboard[i][j] == -1:
                exit[0], exit[1] = i,j
                orgboard[i][j] = 0
    return orgboard

for time in range(1, k+1):
    movePeople()
    board =rotateBoard()
    
print(sum(move))
print(*[i+1 for i in exit])
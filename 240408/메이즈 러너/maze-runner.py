from collections import deque, defaultdict
n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
person = [[-1,-1]]
for _ in range(m):
    x,y = map(int,input().split())
    person.append([x-1, y-1])
exit = list(map(int,input().split()))
exit[0], exit[1] = exit[0]-1, exit[1]-1
personmove = defaultdict(int)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def movePerson():
    ei, ej = exit
    for idx in range(1, 1+m):
        if person[idx] == [-1,-1]:
            continue
        x,y = person[idx]
        org_d = abs(x-ei) + abs(y-ej)
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                new_d = abs(nx-ei) + abs(ny-ej)
                if [nx,ny] == [ei, ej]:
                    personmove[idx] += 1
                    person[idx] = [-1,-1]
                    break
                if new_d < org_d:
                    person[idx] = [nx,ny]
                    personmove[idx] += 1
                    break


def findSquare():
    length = 2
    personboard = [[0]*n for _ in range(n)]
    for i,j in person:
        if [i,j] == [-1,-1]:
            continue
        personboard[i][j] = 1
    search = True
    while search:
        for i in range(0,n-length+1):
            for j in range(0,n-length+1):
                square = [0,0]
                for di in range(length):
                    for dj in range(length):
                        if personboard[i+di][j+dj]:
                            square[0] += 1
                        if [i+di, j+dj] == exit:
                            square[1] += 1

                if square[0] >= 1 and square[1] == 1:
                    selected =[i,j,length]
                    search = False
                    break
            if not search:
                break
        length += 1
    return selected

def rotateSquare(sq):
    si, sj, sl = sq
    newboard = [[0]*sl for _ in range(sl)]
    for i in range(sl):
        for j in range(sl):
            newboard[i][j] = board[si+i][sj+j]
            if [si+i, sj+j] == exit:
                newboard[i][j] = -1
            for pidx, [pi, pj] in enumerate(person):
                if [pi,pj] == [si+i, sj+j]:
                    if newboard[i][j] == 0:
                        newboard[i][j] = [pidx*10]
                    else:
                        newboard[i][j].append(pidx*10)

    newboard_ = list(map(list, zip(*newboard[::-1])))
    for i in range(sl):
        for j in range(sl):
            if type(newboard_[i][j]) == list:
                for idx in newboard_[i][j]:
                    pidx = idx // 10
                    person[pidx] = [si+i, sj+j]
                    board[si+i][sj+j] = 0
                continue
            if newboard_[i][j] == 0:
                board[si+i][sj+j] = newboard_[i][j]
            elif newboard_[i][j] == -1:
                board[si+i][sj+j] = 0
                exit[0], exit[1] = si+i, sj+j
            elif 0<newboard_[i][j]<10:
                board[si+i][sj+j] = newboard_[i][j] -1
                

for time in range(k):
    movePerson()
    if person.count([-1,-1]) == len(person):
        break
    selected = findSquare()
    rotateSquare(selected)

print(sum(personmove.values()))
for i in exit:
    print(i+1, end=' ')
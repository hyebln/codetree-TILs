import heapq

q = int(input())
queries = [list(map(int,input().split())) for _ in range(q)]

def moveRabbit(rabbit):
    global totalsum
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    rj,rxy,rx,ry,ridx = rabbit
    rd = rdist[ridx]
    nextrabbit = [-1,-1]
    for d in range(4):
        nx = (rx+dx[d]*rd)%(2*(n-1))
        ny = (ry+dy[d]*rd)%(2*(m-1))
        nx = min(nx, 2*(n-1)-nx)
        ny = min(ny, 2*(m-1)-ny)
        if (sum(nextrabbit), nextrabbit[0], nextrabbit[1]) < (nx+ny, nx, ny):
            nextrabbit = [nx,ny]
            
    heapq.heappush(rabbitheap, [rj+1, sum(nextrabbit), nextrabbit[0],nextrabbit[1],ridx])
    score[ridx] -= sum(nextrabbit) +2
    totalsum += sum(nextrabbit)+2


rabbitheap= []
score = {}
rdist = {}
totalsum = 0
for query in queries:
    idx, *content = query
    if idx == 100:
        n, m, p, *rabbits = content
        for i in range(0,p*2,2):
            id = rabbits[i]
            d = rabbits[i+1]
            heapq.heappush(rabbitheap, [0,0,0,0,id])
            rdist.setdefault(id, d)
            score.setdefault(id, 0)
            
    if idx == 200:
        k,s = content
        moved = set()
        for turn in range(k):
            selected = heapq.heappop(rabbitheap)
            moveRabbit(selected)
            moved.add(selected[-1])
        last = [-1,-1,-1,-1]
        for rab in rabbitheap:
            rj,rxy,rx,ry,ri = rab
            if ri in moved:
                if (last[0], last[1], last[2], last[3]) < (rxy, rx, ry, ri):
                    last = [rxy, rx, ry, ri]
        score[last[-1]] += s


    if idx == 300:
        rid, L = content
        rdist[rid] = rdist[rid]*L

    if idx == 400:
        maxrabbit = max(score.values())
        print(totalsum+maxrabbit)
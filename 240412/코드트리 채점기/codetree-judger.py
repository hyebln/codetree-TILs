import heapq
from collections import defaultdict


Q = int(input())
QUE = [list(input().split()) for _ in range(Q)]


waitQ = defaultdict(list)
waitingurl = set()
caltime = defaultdict()
endlist = []

for query in QUE:
    q, *inp = query
    if q == '100':
        N, u0 = inp
        calcul = [0] * int(N)
        dom0, id0 = u0.split('/')
        heapq.heappush(waitQ[dom0], [1, 0, int(id0)])
        waitingurl.add(u0)

    if q =='200':
        t,p,u = inp
        if u in waitingurl:
            continue
        dom0, id = u.split('/')
        heapq.heappush(waitQ[dom0], [int(p), int(t), int(id)])
        waitingurl.add(u)

    if q == '300':
        if not 0 in calcul:
            continue

        t = int(inp[0])
        bestdom, best_p, best_t = '', 10e9, 10e9
        for domain, heap in waitQ.items():
            if domain in caltime.keys():
                start, gap = caltime[domain]
                if gap == 0:
                    continue
                if gap!=0 and t < start+3*gap:
                    continue

            if not heap:
                continue

            que = heap[0]
            qp, qt, qid = que
            if (qp, qt) < (best_p, best_t):
                bestdom, best_p, best_t, pid = domain, qp, qt, qid

        if bestdom == '':
            continue

        heapq.heappop(waitQ[bestdom])
        besturl = bestdom +'/'+str(pid)
        for idx, cal in enumerate(calcul):
            if cal == 0:
                calcul[idx] = [bestdom, t]
                caltime[bestdom] = [t,0]
                waitingurl.remove(besturl)
                break

    if q =='400':
        t, Jid = inp
        if calcul[int(Jid)-1] == 0:
            continue
        dom,st = calcul[int(Jid)-1]

        calcul[int(Jid)-1] = 0
        caltime[dom] = [st, int(t)-st]

    if q == '500':
        ans =0
        for val in waitQ.values():
            ans += len(val)
        print(ans)
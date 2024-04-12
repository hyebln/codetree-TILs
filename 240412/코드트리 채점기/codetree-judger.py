import heapq
from collections import defaultdict
q = int(input())
queries = [list(input().split()) for _ in range(q)]

def startCalcul(time):
    available = []
    unavailable = []
    while stanby:
        p,t = heapq.heappop(stanby)
        domain, id = stanbyurl[t].split('/')
        if domain in calcul.values():
            heapq.heappush(unavailable, [p,t])
            continue
        if domain in enddomain.keys():
            curstart, gap = enddomain[domain][-1]
            if time < curstart + 3*gap:
                heapq.heappush(unavailable, [p,t])
            else:
                heapq.heappush(available, [p,t])
            continue
        heapq.heappush(available, [p,t])

    if available == []:
        return unavailable

    selected = heapq.heappop(available)
    for remain in available:
        heapq.heappush(unavailable, remain)

    sp, st = selected
    sdomain, sid = stanbyurl.pop(st).split('/')
    for idx, cur in calcul.items():
        if not cur:
            calcul[idx] = sdomain
            startT[idx] = time
            break

    return unavailable

def endCalcul(time, jidx):
    domain = calcul[jidx]
    st = startT[jidx]
    calcul[jidx] = []
    startT[jidx] = 0
    enddomain[domain].append([st, time-st])

stanby = []
stanbyurl = {}
enddomain = defaultdict(list)
calcul = {}
startT = [0]
for query in queries:
    qtype, *content = query
    if qtype=='100':
        N, u0 = content
        for i in range(1, int(N)+1):
            calcul.setdefault(i, [])
            startT.append(0)
        heapq.heappush(stanby, [1,0])
        stanbyurl.setdefault(0,u0)
    if qtype == '200':
        t,p,u = content
        t, p = int(t), int(p)
        if u not in stanbyurl.values():
            heapq.heappush(stanby, [p,t])
            stanbyurl.setdefault(t, u)
    if qtype == '300':
        t = int(content[0])
        if list(calcul.values()).count([]) == 0:
            continue
        stanby = startCalcul(t)
    if qtype == '400':
        t, jid = int(content[0]), int(content[1])
        if calcul[jid] == []:
            continue
        endCalcul(t, jid)

    if qtype == '500':
        t = int(content[0])
        print(len(stanby))
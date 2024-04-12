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
        if domain in enddomain.keys():
            start, gap = enddomain[domain]
            if gap == 0:
                heapq.heappush(unavailable, [p,t])
            else:
                if time < start + 3*gap:
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
    for idx, cal in enumerate(calcul):
        if idx == 0:
            continue
        if cal == 0:
            calcul[idx] = [sdomain, time]
            enddomain[sdomain] = [time, 0]
            break

    return unavailable

def endCalcul(time, jidx):
    domain, st= calcul[jidx]
    calcul[jidx] = 0
    enddomain[domain]=[st, time-st]

stanby = []
stanbyurl = {}
enddomain = defaultdict(list)
for query in queries:
    qtype, *content = query
    if qtype=='100':
        N, u0 = content
        calcul = [0]*int(int(N)+1)
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
        if not 0 in calcul[1:]:
            continue
        stanby = startCalcul(t)
    if qtype == '400':
        t, jid = int(content[0]), int(content[1])
        if calcul[jid] == 0:
            continue
        endCalcul(t, jid)

    if qtype == '500':
        t = int(content[0])
        print(len(stanby))
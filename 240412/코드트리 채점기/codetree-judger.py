import heapq
from collections import defaultdict
q = int(input())
queries = [list(input().split()) for _ in range(q)]

def startCalcul(time):
    newheapq = []
    bestdom, best_p, best_t = '', 10e9, 10e9
    while stanby:
        p,t = heapq.heappop(stanby)
        domain, id = stanbyurl[t].split('/')
        if domain in enddomain.keys():
            start, gap = enddomain[domain]
            if gap == 0:
                heapq.heappush(newheapq, [p,t])
            else:
                if time < start + 3*gap:
                    heapq.heappush(newheapq, [p,t])
                else:
                    if (best_p, best_t) > (p,t):
                        if bestdom != '':
                            heapq.heappush(newheapq, [best_p,best_t])
                        bestdom, best_p, best_t = domain, p,t
                    else:
                        heapq.heappush(newheapq, [p,t])
            continue

        if (best_p, best_t) > (p, t):
            if bestdom != '':
                heapq.heappush(newheapq, [best_p, best_t])
            bestdom, best_p, best_t = domain, p, t
        else:
            heapq.heappush(newheapq, [p,t])

    if bestdom == '':
        return newheapq

    sdomain, sid = stanbyurl.pop(best_t).split('/')
    for idx, cal in enumerate(calcul):
        if idx == 0:
            continue
        if cal == 0:
            calcul[idx] = [sdomain, time]
            enddomain[sdomain] = [time, 0]
            break

    return newheapq

def endCalcul(time, jidx):
    # print(time,'초에 멈춤', jidx)
    domain, st= calcul[jidx]
    calcul[jidx] = 0
    enddomain[domain]=[st, time-st]

stanby = []
stanbyurl = {}
enddomain = defaultdict(list)
for query in queries:
    qtype, *content = query
    # print('명령어', query)
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
        if 0 in calcul[1:]:
            stanby = startCalcul(t)

    if qtype == '400':
        t, jid = int(content[0]), int(content[1])
        if calcul[jid] == 0:
            continue
        endCalcul(t, jid)

    if qtype == '500':
        t = int(content[0])
        print(len(stanby))
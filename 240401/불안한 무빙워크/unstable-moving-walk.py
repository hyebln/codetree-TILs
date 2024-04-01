n,k = map(int, input().split())
safe = list(map(int, input().split()))
movingwalks = [0]*n


def rotate_mw(org_s, org_mw):
    a = org_s.pop(2*n-1)
    new_s= [a]+org_s

    b = org_mw.pop(n-1)
    new_mw = [0] + org_mw
    return new_s, new_mw

def move_person():
    if movingwalks[n-1]:
        movingwalks[n-1] = 0
    for idx in range(n-2,-1, -1):
        if movingwalks[idx] and not movingwalks[idx+1] and safe[idx+1]>0:
            movingwalks[idx] = 0
            movingwalks[idx+1] = 1
            safe[idx+1] -= 1


    if not movingwalks[0] and safe[0] > 0:
        movingwalks[0] = 1
        safe[0] -= 1


turn = 0
while True:
    turn += 1
    safe, movingwalks = rotate_mw(safe, movingwalks)
    move_person()
    if safe.count(0) >= k:
        break
print(turn)
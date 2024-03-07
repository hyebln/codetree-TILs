n = int(input())
clients = list(map(int, input().split()))
check = list(map(int, input().split()))

answer = 0
for c in clients:
    num = c - check[0]
    answer += 1
    if num <= 0:
        continue
    
    another = num // check[1]
    remain = num % check[1]
    
    answer += another
    if remain >0 :
        answer += 1
print(answer)
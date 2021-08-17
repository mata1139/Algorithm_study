N = int(input())
adventure = list(map(int,input().split()))
answer = 0

adventure.sort()
count = 0

for horror in adventure:
    count += 1

    if count >= horror :
        answer += 1
        count = 0

print(answer)


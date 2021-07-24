import sys
from collections import deque
N = int(input())

numbers = [int(input())-1 for i in range(N)]
checked = [False for i in range(N)]
answer = set()
visited = deque()

def dfs(idx, visit):
    if checked[idx]:
        if numbers[idx] in visit:
            while visit[0] != idx:
                visit.popleft()

            for element in visit:
                answer.add(element)


    else:
        checked[idx] = True
        visit.append(idx)
        dfs(numbers[idx],visit)




for i in range(N):
    if not checked[i]:
        dfs(i,visited.copy())


print(len(answer))
for element in sorted(list(answer)):
    print(element+1)



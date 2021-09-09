import sys
from collections import deque

input = sys.stdin.readline  # 시간초과를 방지하기 위해 사용,

N,M,K,X = map(int,input().split()) # N,M,K,X 입력

MAP = [[] for i in range(N+1)]     # 지도 초기화,
visited = [0 for i in range(N+1)]  # 방문 여부 및 거리 저장,


for i in range(M):                 # 도로 정보 입력,
    start,end = map(int,input().split())
    MAP[start].append(end)         # 인접 리스트 사용,

que = deque([X])                   # 처음 방문지 큐에 삽입,


while que:                         # 큐에 원소가 존재 할 동안,
    now = que.popleft()            # 맨 첫번째 원소를 POP,
    
    for road in MAP[now]:          # 해당 지점의 길을 조사,
        
        if visited[road] == 0: # 방문한 적이 없는 곳이라면,
            visited[road] = visited[now] + 1 # 현재 지점까지의 거리 + 1  
            que.append(road)       # 큐에 해당 지점 추가,

if not K in visited:               # 거리가 k인 지점이 없다면 -1 출력,
    print(-1)

else:                             
    for i in range(N+1):           # 거리가 K인 지점 모두 출력,
        if visited[i] == K:
            print(i)

from collections import deque
dy = [1,-1,0,0]  # y 방향
dx = [0,0,-1,1]  # x 방향

N,K = map(int,input().split())

info = [] # 시험관

virus = [[] for i in range(K)] # virus 종류별 위치 저장 리스트

for i in range(N): # 시험관 정보 입력
    info.append(list(map(int,input().split())))

S,X,Y = map(int,input().split()) # S, X, Y 입력

for i in range(N):
    for j in range(N):
        if info[i][j] != 0:
            virus[info[i][j]-1].append((info[i][j],i,j)) # virus 종류별 초기 위치 저장

que = deque() # BFS를 위한 deque

que.append(virus) # deque에 virus 정보 삽입

time = 0 # 시간 counting

while que:

    tmp_element = [] # 같은 virus를 묶기위한 list
    tmp_category = [] # 같은 시간을 묶기 위한 list

    now = que.popleft() # 현재 시간에 전이 되어야 할 virus들  pop

    for category in now:
        for element in category:
            for direct in range(4):  # dx, dy를 이용하여 체크
                x = element[1] + dx[direct]
                y = element[2] + dy[direct]


                if x >= 0 and x < N and y >= 0 and y < N: # 시험관을 벗어나지 않는다면,

                    if info[x][y] == 0                    # 아직 전염 되지 않은 곳이라면,
                        info[x][y] = element[0]           # 해당 virus 로 전염 시킨다.
                        tmp_element.append((element[0],x,y)) # 해당 위치 다시 que에 삽입

        if tmp_element:
            tmp_category.append(tmp_element) # 같은 virus 끼리 tmp_category로 묶기

    if tmp_category:
        que.append(tmp_category) # que에 삽입

    time += 1 # 시간 증가

    if time == S: # 시간이 S라면 break,
        break

print(info[X-1][Y-1]) # X,Y 정보 출력

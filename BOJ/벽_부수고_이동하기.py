import copy
from collections import deque

N, M = input().split()
N = int(N)
M = int(M)

Maze = []
for i in range(N):
    Maze.append(list(input()))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]



def bfs(origin_x, origin_y, maze):
    global N
    global M
    visit = [[[0 for i in range(M)] for j in range(N) ] for k in range(2)]


    q = deque()
    q.append((origin_x,origin_y,False,1))
    visit[0][origin_x][origin_y] = 1
    visit[1][origin_x][origin_y] = 1

    while q:
        x,y,brake,cost = q[0]
        q.popleft()


        for idx in range(4):
            tmp_x = x + dx[idx]
            tmp_y = y + dy[idx]

            if tmp_x >= 0 and tmp_x < N and tmp_y >=0 and tmp_y < M:
                if tmp_x == N-1 and tmp_y == M-1:
                    return cost+1

                if maze[tmp_x][tmp_y] =='0':
                    if brake and visit[1][tmp_x][tmp_y] == 0:
                        visit[1][tmp_x][tmp_y] = 1
                        q.append((tmp_x, tmp_y,brake,cost+1))

                    elif not brake and visit[0][tmp_x][tmp_y] == 0:
                        visit[0][tmp_x][tmp_y] = 1
                        q.append((tmp_x, tmp_y,brake,cost+1))



                elif maze[tmp_x][tmp_y] =='1' and not brake and visit[1][tmp_x][tmp_y] == 0:
                    visit[1][tmp_x][tmp_y] = 1
                    q.append((tmp_x, tmp_y, True, cost + 1))



    return 1 if N == 1 and M == 1 else -1


print(bfs(0, 0,Maze))

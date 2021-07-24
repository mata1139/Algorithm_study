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

    visit = [[0 for i in range(M)] for j in range(N) ]

    q = deque()
    q.append((origin_x,origin_y))
    visit[origin_x][origin_y] = 1

    while q:
        x,y = q[0]
        q.popleft()


        for idx in range(4):
            tmp_x = x + dx[idx]
            tmp_y = y + dy[idx]

            if tmp_x >= 0 and tmp_x < N and tmp_y >=0 and tmp_y < M:
                if maze[tmp_x][tmp_y]!='0' and visit[tmp_x][tmp_y] == 0:
                    visit[tmp_x][tmp_y] = visit[x][y] + 1

                    if tmp_x == N-1 and tmp_y == M-1:
                        return visit[tmp_x][tmp_y]

                    q.append((tmp_x,tmp_y))

print(bfs(0, 0,Maze))



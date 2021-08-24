from collections import deque 

dx = [0,1,0,-1] # dx
dy = [1,0,-1,0] # dy
didx = 0        # dx,dy 접근 idnex

snake = deque() # 뱀의 몸 저장,
snake.append([1,1]) # 초기 값 1,1

apple = []      # 사과 위치,
direction = []  # 방향 변환,
answer = 0      

N = int(input())
K = int(input())

for i in range(K): # 사과 위치 입력,
    apple.append(list(map(int,input().split())))

L = int(input())

for i in range(L): # 방향 전환 입력,
    direction.append(list(map(str,input().split())))

while True:
    if direction: # 방향 리스트가 비어있지 않으면,
        
        if int(direction[0][0]) == answer: # 방향 전환을 해야하는 시간일 때,
            
            if direction[0][1] == 'L':     # L이면 왼쪽 전환
                didx -=1                   # didx--
                
            else:                          # D이면 오른쪽 전환,
                didx += 1                  # didx++


            if didx < 0:                   # didx가 -1 일 때, 
                                           # 즉, didx가 0 일때 L이 나오면,
                didx = 3                   
                                           
            else:                          # 4개의 값으로 순환
                didx %= 4
                
            del direction[0]               # 방향 전환 후, direction 리스트에서 제거

    head_row = snake[0][0] + dx[didx]      # 해당 방향으로 전진,
    head_col = snake[0][1] + dy[didx]      # 해당 방향으로 전진,

    if head_row >=1 and head_row <= N and head_col >= 1 and head_col <= N and ([head_row,head_col] not in snake) : # 맵을 벗어나지 않고, 뱀의 몸통에 닿지 않으면,
        
        if [head_row,head_col] in apple:                   # 해당 위치에 사과가 존재하면,
            
            apple.remove([head_row,head_col])              # 사과 리스트에서 제거,
            snake.appendleft([head_row,head_col])          # 꼬리를 남긴다.
            
        else:                                              # 사과가 없으면,
            
            snake.pop()                                    # 꼬리제거,
            snake.appendleft([head_row,head_col])

        answer += 1                                        # 시간 증가,
        

    else:                                                  # 종료조건에 해당되면,
        answer += 1                                        # 시간 증가 후 break,
        break

print(answer)






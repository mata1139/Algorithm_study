N = input() 

front = N[:int(len(N)/2)]  # 숫자의 왼쪽 부분,
rear = N[int(len(N)/2):]   # 숫자의 오른쪽 부분,
check = 0


for idx in range(len(front)): # 왼쪽 부분과 오른쪽 부분 자릿수들의 차의 합이 0이면, LUCKY
                              # 123 / 402
                              # (1-4) + (2-0) + (3-2) = 0 → LUCKY
    
    sum = int(front[idx]) - int(rear[idx]) # 각 자릿수의 차
    check += sum                          

if check == 0:
    print("LUCKY")
else:
    print("READY")

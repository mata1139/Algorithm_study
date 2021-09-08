from itertools import permutations # 순열 사용

N = int(input())                           # N, 숫자, 연산자 개수 입력
numbers = list(map(int,input().split()))
op_cnt = list(map(int,input().split()))

op = []                                    # 연산자가 저장될 리스트,

op.extend('+' * op_cnt[0])                 # 각 연산자의 개수만큼 생성,
op.extend('-' * op_cnt[1])
op.extend('*' * op_cnt[2])
op.extend('/' * op_cnt[3])

result = []                                # 각 식에 대한 연산 결과가 저장,

for i in set(list(permutations(op,len(op)))): # 연산자를 이용하여

    value = numbers[0]                     # 식을 계산하기 위하여, 첫 번 째 수를 미리 저장

    for a,b in zip(numbers[1:],i):         # zip을 이용해, 각 차례에 맞는 숫자와 연산자를 묶는다.
                                           # ex) ('+','+','*','/','-') [2,3,4,5,6]
                                           # 2 +
                                           # 3 +
                                           # 4 * ...

        if b == '/':                       # 연산자가 나눗셈이라면,

            if value < 0:                  # 음수 일때,
                value = -(abs(value)//a)   # 파이썬에서는 음수 몫을 계산할 때, 내림을 이용하기 때문에
                                           # 절댓값으로 변경을 하지않고서 계산시, 답이 달라진다.

            else:                          # 양수 일때,
                value = value//a

        else:
            value = eval(str(value) + b + str(a)) # eval을 이용하여 식을 계산,

    result.append(value) # result 리스트에 결과값 append


print(min(result)) # 최소, 최대 출력
print(max(result))

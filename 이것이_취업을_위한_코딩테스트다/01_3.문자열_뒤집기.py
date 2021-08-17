'''
0001100 → 0 과 1 의 뭉텅이 들 중, 더 작은 개수의 뭉텅이를 전부 뒤집어 주면 최소이다.
0 → [000,00]
1 → [11]
1을 전부 뒤집어 주면, 최소이다. 1번
'''

string = input()  # 문자열 입력

first = 0  # 처음 반복되는 숫자들의 뭉텅이 수 ex) 0001100111 → 000 , 00
second = 0 # 두번째로 반복되는 숫자들의 뭉텅이 수 ex) 0001100111 → 11 , 111

ch = string[0] # 처음 시작하는 숫자
check = True # first 와 second에 순서대로 반복하며, 저장하기 위한 Flag

for char in string: # 모든 숫자를 순회하면서,

    if char != ch: # 연속되지 않는 숫자가 나올 시,

        if check: # first에 저장 될 차례 일 때,
            first += 1 # 뭉텅이 수 ++
            check = False

        else: # second에 저장 될 차례 일 때,
            second += 1 # 뭉텅이 수 ++
            check = True

        ch = char # 비교하는 숫자를 갱신,

# 마지막 뭉텅이++
if check:
    first += 1

else:
    second += 1

print(min(first,second))

'''
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
'''

def solution(number, k):
    stack = [] # Stack 자료형 선언
    
    for num in number: # 모든 Number에 대해,
        
        if not stack:  # 스택 비어있으면,
            stack.append(num) # Num 삽입,
            
        else:          # 스택에 자료가 존재하면,
            
            while stack: # 스택이 비어있지 않을 동안,
                
                if stack[-1] < num and k > 0: # 마지막 원소가 받은 Num 보다 작고,
                                              # K 가 0 보다 크다면,
                    stack.pop()               # Pop,
                    k -= 1                    # k--,
                    
                else:                         # 마지막 원소가 더 크다면, break
                    break
                
            stack.append(num)                 # Num 삽입,
    
    if k > 0:                                 # K가 남았을 때,
        for _ in range(k):                    # 뒤에서 부터, K 만큼 pop
            stack.pop()
    
    return ''.join(stack)                     # Join 을 통해 Return

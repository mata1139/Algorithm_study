'''
문제 설명
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
입출력 예
s	      answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false
'''

def solution(s):
    answer = True
    stack = []               #Stack 선언
    
    try:                     
        for paren in s:     
            if paren=='(':   #'(' 면 Stack 삽입
                stack.append('(')
            else:            #')' 면 pop
                stack.pop()
    except:                  #pop 연산 중 예외 발생 시 return False
        return False
    
    if not stack:            #스택이 비어있으면, 정상
        return True
    else:
        return False


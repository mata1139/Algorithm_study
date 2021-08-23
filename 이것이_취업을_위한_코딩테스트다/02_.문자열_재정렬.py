string = list(input())

sum = 0      # 숫자 처리,
answer = ""  # 알파벳 처리,

for char in string: # 순회,
    
    if char.isdigit():   # 숫자이면,
        sum += int(char) # sum에 더해준다,
    else:                # 문자이면,
        answer = answer + char # answer에 concatenate


answer = answer + str(sum) # answer에 sum concatenate

print(answer)



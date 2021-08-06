'''
def solution(n, words):
    answer = [0,0]  # Default,

    people = [[] for i in range(n)] # 사람 별 단어,
    all_words = [] # 전체 단어, 중복 여부 Check용,
    last_char = words[0][0] # 이전 단어의 마지막 문자 저장 변수,
   
    for idx in range(len(words)): # words의 모든 단어 순회,
       
        index = idx % n # People index에 접근하기 위함,
        people[index].append(words[idx]) # 사람 별 단어 List에 추가,
       
        
        if last_char == words[idx][0] and words[idx] not in all_words: # 시작 문자가 끝말과 같거나, 중복되지 않으면,
            last_char = words[idx][-1] # last_char 갱신,
            all_words.append(words[idx]) # 전체 단어 List 추가,
        
        else:                                        # 탈락자 발생 경우,
            answer = [index+1,len(people[index])] # answer 값 Update
            return answer                         # Return

    return answer                                 # 탈락자 없는 경우, [0,0] Return
'''


def solution(n, words):
    answer = [0,0]  # Default,

    people = [[] for i in range(n)] # 사람 별 단어,
    all_words = [] # 전체 단어, 중복 여부 Check용,
    last_char = words[0][0] # 이전 단어의 마지막 문자 저장 변수,
   
    for idx in range(len(words)): # words의 모든 단어 순회,
       
        index = idx % n # People index에 접근하기 위함,
        people[index].append(words[idx]) # 사람 별 단어 List에 추가,
       
        
        if last_char == words[idx][0] and words[idx] not in all_words: # 시작 문자가 끝말과 같거나, 중복되지 않으면,
            last_char = words[idx][-1] # last_char 갱신,
            all_words.append(words[idx]) # 전체 단어 List 추가,
        
        else:                                        # 탈락자 발생 경우,
            answer = [index+1,len(people[index])] # answer 값 Update
            return answer                         # Return

    return answer                                 # 탈락자 없는 경우, [0,0] Return

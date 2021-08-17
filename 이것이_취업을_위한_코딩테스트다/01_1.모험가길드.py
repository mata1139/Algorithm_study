N = int(input()) # N 입력
adventure = list(map(int,input().split())) # 모험가 리스트 입력

answer = 0 # 최종 그룹 수

adventure.sort() # 공포도 순으로 정렬
count = 0        # 그룹 내 인원 수

for horror in adventure: # 모험가 전체를 순회,
    count += 1           # 그룹 인원수++

    if count >= horror : # 그룹 인원수가 현재 모험가 공포도 보다 크거나 같다면,
        answer += 1      # 그룹 자르기,
        count = 0        # 인원수 

print(answer)


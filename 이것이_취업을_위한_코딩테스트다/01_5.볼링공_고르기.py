N,M = map(int,input().split()) # N,M 입력
ball = list(map(int,input().split())) # 공 무게 List 저장,

ball_dict = {} # 무게 : 갯수 Dictionary 생성

result = 0 # 최종 가능한 조합 수

for weight in ball: # Dictionary 초기화 과정,
    ball_dict[weight] = ball.count(weight) # 공 무게 : 개수

for count in ball_dict.values(): # 모든 Value 들 즉, 무게 별 공 갯수에 대해,
    N -= count # 현재 무게 갯수를 제외한 공의 갯수를 계산,
    result += count * N # A가 현재 무게의 공을 선택 했을 때, 가능한 조합의 수를 result에 더한다.

print(result)

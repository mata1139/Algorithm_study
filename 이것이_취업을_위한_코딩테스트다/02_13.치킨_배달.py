from itertools import combinations # 조합 활용,

N,M = map(int,input().split())
city = []                          # 도시의 지도,
result = []                        # 각 조합에 따른, 도시거리 저장,


for i in range(N):                 # 도시 지도 초기화,
    city.append(list(map(int,input().split())))


homes = []                         # 집의 좌표 저장,
chicken = []                       # 치킨집 좌표 저장,

for i in range(N):                 # 집과 치킨집의 좌표를 초기화 하는 부분,
    for j in range(N):
        if city[i][j] == 1:
            homes.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

combi = list(combinations(chicken,M)) # 치킨집의 좌표로 조합을 생성,


for i in range(len(combi)):           # 모든 조합에 대해,
    city_distance = 0                 # 각 조합 별 도시 거리,
    
    for home in homes:                # 모든 집을 순회,
        
        tmp_distance = []             
        for combi_x,combi_y in combi[i]:  # 해당 집과 모든 치킨집에 대한 치킨 거리 저장,
            tmp_distance.append(abs(home[0]-combi_x) + abs(home[1]-combi_y))
            
        city_distance += min(tmp_distance) # 가장 작은 거리의 치킨 거리가 해당 집의 치킨 거리, 따라서, 도시 거리에 더해준다.

    result.append(city_distance)           # 해당 조합에 대해, 탐색이 종료되었으면, result에 추가

print(min(result))                   # 가장 최소인 경우를 출력,



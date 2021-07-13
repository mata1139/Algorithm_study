'''
프렌즈4블록
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.


블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.


만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.

위 초기 배치를 문자로 표시하면 아래와 같다.

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

입력 형식
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
2 ≦ n, m ≦ 30
board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
출력 형식
입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.

입출력 예제
m	n	board	answer
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
예제에 대한 설명
입출력 예제 1의 경우, 첫 번째에는 A 블록 6개가 지워지고, 두 번째에는 B 블록 4개와 C 블록 4개가 지워져, 모두 14개의 블록이 지워진다.
입출력 예제 2는 본문 설명에 있는 그림을 옮긴 것이다. 11개와 4개의 블록이 차례로 지워지며, 모두 15개의 블록이 지워진다.
'''

import numpy as np 

def solution(m, n, board):
    answer = 0
    
    board_arr = [ list(element) for element in board] # board 2차원 List로 생성,
    
    
    dx = [1,0,1] # 옆, 아래, 대각선 아래  x,y 증가량,
    dy = [0,1,1]
    
    while(True):
        
        boom = [] # 터트릴 블록 저장 List,
        
        for row in range(m): # 모든 블록 각각에 대해,
            for col in range(n):
               
                if (board_arr[row][col] != '-1'): # 블록이 존재하면,
                    tmp_boom = [(row,col)]        # tmp_boom 에 터트릴 블록 좌표 저장,
                    count = 1                     # 같은 블록 개수 저장,
                    
                    for i in range(3):            # 옆, 아래, 대각선 아래 블록에 대해,
                        tmp_row = row + dx[i]
                        tmp_col = col + dy[i]
                        
                        if tmp_row < m and tmp_col < n: # board 판에 존재하는 블록일 시,
                            
                            # 현재 블록과 같은 블록이면,
                            if board_arr[row][col] == board_arr[tmp_row][tmp_col]:
                                count += 1 # 같은 블록 개수 ++
                                tmp_boom.append((tmp_row,tmp_col)) # tmp_boom 에 추가
                                
                            else: # 같은 블록이 아니면 loop-break
                                break
                    else: # 정상적으로, for-loop 종료시,
                        if count == 4: # 같은 블록 개수가 4개 일시,
                            boom = boom + tmp_boom # boom List에 tmp_boom 추가,
        
        if boom: # boom이 비어있지 않다면,
            
            answer += len(set(boom)) # answer에 터트릴 블록 개수 더해줌,
            
            for x,y in set(boom):    # 블록을 터트린다 → -1 로 변경
                board_arr[x][y] = '-1'
        
        
            '''  Source      Transpose   1을 앞으로    Transpose
            ex) C C B D E     C 1 1 C     1 1 C C     1 1 1 D E
                1 1 1 D E     C 1 1 C     1 1 C C     1 1 1 D E
                1 1 1 B F  →  B 1 1 B  →  1 1 B B  →  C C B B F
                C C B B F     D D B B     D D B B     C C B B F
                              E E F F     E E F F 
            '''
            
            trans = np.array(board_arr).T.tolist() # 블록을 아래로 밀기 위해 전치행렬로 변환,
            
          
            for row in trans: # 각 row 마다 접근,
                count = row.count('-1')        # -1의 개수를 저장,    
            
                for _ in range(count):       # -1를 모두 제거,
                    row.remove('-1')               
            
                for _ in range(count):
                    row.insert(0,'-1')   # -1을 모두 제거 후, 개수만큼 앞에서 부터 삽입
            board_arr = np.array(trans).T.tolist() # 다시 전치행렬을 이용해, 변환
            
        else: # boom이 비어있다면 즉, 터트릴 블록이 없을 시 while-break
            break

    return answer


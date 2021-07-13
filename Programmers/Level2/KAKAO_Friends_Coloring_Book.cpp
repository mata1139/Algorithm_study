/*
카카오 프렌즈 컬러링북
출판사의 편집자인 어피치는 네오에게 컬러링북에 들어갈 원화를 그려달라고 부탁하여 여러 장의 그림을 받았다. 여러 장의 그림을 난이도 순으로 컬러링북에 넣고 싶었던 어피치는 영역이 많으면 색칠하기가 까다로워 어려워진다는 사실을 발견하고 그림의 난이도를 영역의 수로 정의하였다. (영역이란 상하좌우로 연결된 같은 색상의 공간을 의미한다.)

그림에 몇 개의 영역이 있는지와 가장 큰 영역의 넓이는 얼마인지 계산하는 프로그램을 작성해보자.

alt text

위의 그림은 총 12개 영역으로 이루어져 있으며, 가장 넓은 영역은 어피치의 얼굴면으로 넓이는 120이다.

입력 형식
입력은 그림의 크기를 나타내는 m과 n, 그리고 그림을 나타내는 m × n 크기의 2차원 배열 picture로 주어진다. 제한조건은 아래와 같다.

1 <= m, n <= 100
picture의 원소는 0 이상 2^31 - 1 이하의 임의의 값이다.
picture의 원소 중 값이 0인 경우는 색칠하지 않는 영역을 뜻한다.
출력 형식
리턴 타입은 원소가 두 개인 정수 배열이다. 그림에 몇 개의 영역이 있는지와 가장 큰 영역은 몇 칸으로 이루어져 있는지를 리턴한다.

예제 입출력
m	n	picture	answer
6	4	[[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]	[4, 5]
예제에 대한 설명
예제로 주어진 그림은 총 4개의 영역으로 구성되어 있으며, 왼쪽 위의 영역과 오른쪽의 영역은 모두 1로 구성되어 있지만 상하좌우로 이어져있지 않으므로 다른 영역이다. 가장 넓은 영역은 왼쪽 위 1이 차지하는 영역으로 총 5칸이다.
*/

#include <vector>
#include <queue>

using namespace std;
int M;  // m의 전역변수,
int N;  // n의 전역변수,

int dx[] = {0,0,-1,1}; // 상,하,좌,우 의 x,y 증가량
int dy[] = {1,-1,0,0};


int bfs(int i,int j,vector<vector<int>> &picture)  // BFS,
{
    int x,y;                      // Area의 첫 x,y 좌표
    int areaSize = 1;             // Area의 크기, 초기값 1
    int color = picture[i][j];    // 현재 Area의 Color
    queue<pair<int,int>> q;       // BFS를 위한 Queue
    
    q.push(pair<int,int>(i,j));   // 첫 x,y 좌표를 Queue에 Push
    picture[i][j] = -1;           // 방문 표시,
    
    while(!q.empty())             // Queue가 비어있지 않을 동안,
    {
        x = q.front().first;      // Queue의 첫 원소의 x,y를 받아온다.
        y = q.front().second;
        q.pop();                  // Queue에서 제거,
        
        for(int i=0;i<4;i++)      // pop한 좌표에서 상,하,좌,우를 기준으로 Color 체크,
        {
            int nx = x +dx[i];
            int ny = y+ dy[i];
            
            if((nx>=0 && ny>=0) && (nx < M && ny < N)) // Picture 크기를 벗어 나지 않으면,
            {
                if(picture[nx][ny] == color)           // 현재 Area의 Color와 동일하면,
                {
                    picture[nx][ny] = -1;              // 방문표시,
                    q.push(pair<int,int>(nx,ny));      // Queue에 Push
                    areaSize++;                        // Area 크기 ++
                }
            }          
        }               
    }
    
    return areaSize;
     
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    
    M = m;  // 크기 전역변수로 설정,
    N = n;
        
    for(int i =0; i<m;i++)        // Picture의 모든 좌표 Color 에 대해,
    {
        for(int j=0; j<n;j++)
        {         
            if(picture[i][j]!=0 && picture[i][j]!=-1) // 0이 아니며, 방문 하지 않았으면,
            {
                int areaSize = bfs(i,j,picture);      // BFS를 통해, Area Size 도출,
              
                if(areaSize > max_size_of_one_area)   // max_size 보다 클 시, 교체,
                    max_size_of_one_area = areaSize;
                number_of_area++;                     // 영역의 수 ++
            }           
        }      
    }
    
 
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}



//다른 사람의 풀이
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int M,N;
int dy[4]={0,-1,0,1};
int dx[4]={-1,0,1,0};
bool visit[100][100]; //방문표시를 위한 2차원 배열

int countArea(const vector<vector<int>> &picture,int y,int x,int type){
    visit[y][x]=true;
    int ret=1;

    for(int i=0;i<4;i++){
        int ny=y+dy[i];
        int nx=x+dx[i];
        // 영역의 범위를 벗어나거나 방문한 적 있으면 continue
        if(ny<0 || nx<0 || ny>=M || nx>=N || visit[ny][nx]) continue;
        // 영역의 종류가 다르면 continue
        if(picture[ny][nx]!=type) continue;
        
        // 재귀함수 호출 -> DFS
        ret+=countArea(picture,ny,nx,type);
    }

    return ret;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    M=m,N=n;
    // 영역의 개수, 가장 큰 영역의 크기
    int countRegions=0,maxRegion=0;
    
    // 전역변수 visit 초기화
    memset(visit,0,sizeof(visit));

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(!visit[i][j] && picture[i][j]!=0){ // 방문 하지 않았으며, 0이 아닐 경우,
                countRegions++;  // 영역 개수 ++
                maxRegion = max(maxRegion, countArea(picture,i,j,picture[i][j])); // DFS 함수 실행
            }
        }
    }
    return {countRegions,maxRegion};
}

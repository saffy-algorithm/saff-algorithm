dr = [1,0,-1,0]
dc = [0,1,0,-1]

def dfs(r,c):
    global complex_count   # 전역 변수 사용 (단지 크기 세는 용도)

    # 현재 좌표 (r,c)가 집(1)인 경우에만 탐색 진행
    if square[r][c] == 1:
        square[r][c] = 0        # 방문 처리: 다시 안 오도록 0으로 바꿈
        complex_count += 1      # 단지 내 집 개수 1 증가

        # 상하좌우 네 방향으로 재귀 탐색
        for idx in range(4):
            nr, nc = r + dr[idx], c + dc[idx]   # 다음 좌표
            # 유효한 인덱스인지 확인 (0 <= nr, nc < N)
            if 0 <= nr < N and 0 <= nc < N:
                dfs(nr, nc)     # 다음 좌표에서 다시 DFS 진행

# ------------------- 메인 코드 -------------------

N = int(input())
square = [list(map(int,input())) for _ in range(N)]

count_list = []   # 각 단지의 크기를 저장할 리스트

# 모든 칸을 순회하면서, 집(1)을 만나면 DFS로 단지를 하나 다 탐색
for r in range(N):
    for c in range(N):
        if square[r][c] == 1:   # 아직 방문하지 않은 집 발견
            complex_count = 0   # 새 단지 크기 카운트 초기화
            sr, sc = r, c       # 시작 좌표 저장 (굳이 없어도 되지만 의미 구분용으로 둠)
            dfs(sr,sc)          # DFS 실행, complex_count가 채워짐
            count_list.append(complex_count)   # 해당 단지 크기를 리스트에 추가

# 출력 형식 맞추기
count_list.sort()            # 단지 크기 오름차순 정렬
print(len(count_list))       # 총 단지 수
for _ in count_list:         # 각 단지 크기 한 줄씩 출력
    print(_)

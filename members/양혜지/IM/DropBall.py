# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0  # 최대 이동 횟수를 저장할 변수 초기화
    
    # 처음 시작 좌표
    for r in range(N):
        for c in range(N):
            count = 1  # 시작점도 포함하므로 초기값 1
            pre_r, pre_c = r, c  # 밑에 while문에서는 초기 좌표가 계속 움직이니까, 현재 위치 좌표를 지금 저장
            # 최소값을 현재 시작 좌표로 설정
            min_r, min_c = pre_r, pre_c
            min_number = arr[pre_r][pre_c]
            
            while True:
                # 상하좌우 4방향 탐색
                for k in range(4):
                    nr = pre_r + dr[k]
                    nc = pre_c + dc[k]
                    
                    # nr nc가 유효하다면 유효한 상하좌우값 중에 가장 작은 값과 작은 값의 좌표 찾기
                    if 0 <= nr < N and 0 <= nc < N:
                        # 현재 최소값보다 작은 값이 있으면 갱신
                        if arr[nr][nc] < min_number:
                            min_number = arr[nr][nc]
                            min_r, min_c = nr, nc
                    # 5개 중 최소값과 좌표값 찾음
                
                # 상하좌우 중 더 작은 값이 없으면 (지금은 자기 자신이 최소값)
                # 더 이상 이동할 곳이 없으니 while 종료
                if min_r == pre_r and min_c == pre_c:
                    # 최대 이동 횟수 갱신했어
                    max_count = max(max_count, count)
                    break
                
                # 최소값 위치로 가야댐
                pre_r, pre_c = min_r, min_c
                count += 1
                
    print(max_count)    
# di, dj 는 방향벡터 (방향만 나타내는 값)
# c 는 그 방향으로 얼마나 멀리 갈지 (거리를 나타냄)
# 둘을 곱해서 거리만큼 떨어진 좌표를 구함
# ni, nj 는 새로운 변수
# if 문으로 배열 범위 체크해서 안전하게 누적

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 십자 상하좌우
    # ten_di = [-1, 1, 0, 0]
    # ten_dj = [0, 0, 1, -1]
    max_v = 0

    for i in range(N):
        for j in range(N):
            ten_sum = arr[i][j] # 중심좌표값을 합계에 먼저 포함시켜야됨 (여기서 시작할고임)
            for di, dj in [[-1,0],[1,0],[0,1],[0,-1]]:
                for c in range(1, M):
                    ni, nj = i+di*c, j+dj*c
                    if 0 <= ni < N and 0 <= nj < N:
                        ten_sum += arr[ni][nj]

            if ten_sum > max_v:
                max_v = ten_sum

    # 대각선
    # dia_di = [-1, -1, 1, 1]
    # dia_dj = [-1, 1, -1, 1]

    for i in range(N):
        for j in range(N):
            dia_sum = arr[i][j] # 중심값
            for di, dj in [[-1,-1],[-1,1],[1,-1],[1,1]]:
                for c in range(1, M):
                    ni, nj = i+di*c, j+dj*c
                    if 0 <= ni < N and 0 <= nj < N:
                        dia_sum += arr[ni][nj]

            if dia_sum > max_v:
                max_v = dia_sum

    print(f"#{tc} {max_v}")
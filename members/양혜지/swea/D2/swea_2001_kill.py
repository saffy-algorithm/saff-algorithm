# N, M = map(int,input().split())

# # 1차원 리스트
# arr = list(map(int,input().split()))
# max_val = 0
# for i in range(N-M+1):
#     # 시작점이 달라질 때마다 다른 부분을 봄
#     # 변수 초기화
#     sum_arr = 0
#     for p in range(i, i+M):
#         sum_arr += arr[p]
        
#     max_val = max(max_val, sum_arr)
    
# print(max_val)

###################################

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())

    # 2차원 리스트
    arr = [list(map(int,input().split())) for _ in range (N)]
    max_val = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_arr = 0
            for p in range(i, i+M):
                for q in range(j, j+M):
                    sum_arr += arr[p][q]
            
            # j가 바뀔 때마다 갱신
            max_val = max(max_val, sum_arr)
        
    print(f'#{tc} {max_val}')
# 고대 유적 2


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # N * M 행렬
    raw = [list(map(int, input().split())) for _ in range(N)]
    # M * N 행렬
    raw_vertical = [line for line in zip(*raw)]

    raw_all = raw + raw_vertical
    count_list = [0]

    for line in raw_all:
        count_one = 0
        for num in line:
            if num == 1:
                count_one += 1
            else:
                if count_one >= 2:
                    count_list.append(count_one)
                count_one = 0
        if count_one >= 2:
                count_list.append(count_one)
    
    answer = max(count_list)
    
    print(f"#{tc} {answer}")



# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())

#     # N * M 행렬
#     raw = [list(map(int, input().split())) for _ in range(N)]
    
#     count_list = []
    
#     # 행 '1' 카운트
#     for i in range(N):
#         count_one = 0
#         for j in range(M):
#             if raw[i][j] == 1:
#                 count_one += 1
#             else:
#                 if count_one >= 2:
#                     count_list.append(count_one)
#                 count_one = 0
#         if count_one >= 2:
#                     count_list.append(count_one)
            
#     # 열 '1' 카운트
#     for j in range(M):
#         count_one = 0
#         for i in range(N):
#             if raw[i][j] == 1:
#                 count_one += 1
#             else:
#                 if count_one >= 2:
#                     count_list.append(count_one)
#                 count_one = 0
#         if count_one >= 2:
#                     count_list.append(count_one)
    
#     if count_list:
#         answer = max(count_list)
#     else:
#         answer = 0
    
#     print(f"#{tc} {answer}")

# 풍선팡 보너스게임2

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    
    raw_vertical = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            raw_vertical[i][j] = raw[j][i]

    sum_i_list = []
    sum_j_list = []

    for i_list in raw:
        sum_i_list.append(sum(i_list))

    for j_list in raw_vertical:
        sum_j_list.append(sum(j_list))

    sum_nums = []
    for i in range(N):
        for j in range(N):
            sum_check = sum_i_list[i] + sum_j_list[j] - raw[i][j]
            sum_nums.append(sum_check)

    print(f"#{tc} {max(sum_nums)}")

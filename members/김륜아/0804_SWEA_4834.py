# 숫자카드

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().strip()))
    COUNT = [0] * 10
    for i in range(len(N_list)):
        COUNT[N_list[i]] += 1

    max_count_num = max(COUNT)

    for i in range(9, -1, -1):
        if COUNT[i] == max_count_num:
            print(f"#{tc} {i} {max_count_num}")
            break
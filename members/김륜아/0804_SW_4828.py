# T = int(input())

# for tc in range(1, T+1):
#     A = int(input())
#     raw = list(map(int, input().split()))
#     max_num = max(raw)
#     min_num = min(raw)
#     answer = max_num - min_num
#     print(f"#{tc} {answer}")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    raw = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(N-1-i):
            if raw[j] > raw[j+1]:
                raw[j], raw[j+1] = raw[j+1], raw[j]
    answer = raw[N-1] - raw[0]
    print(f"#{tc} {answer}")
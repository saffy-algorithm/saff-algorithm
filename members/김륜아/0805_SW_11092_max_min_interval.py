# 최대 최소 간격

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_raw = list(map(int, input().split()))

    for i in range(N):
        if N_raw[i] == min(N_raw):
            min_idx = i
            break
    for i in range(N-1,-1,-1):
        if N_raw[i] == max(N_raw):
            max_idx = i
            break

    print(f"#{tc} {abs(max_idx - min_idx)}")

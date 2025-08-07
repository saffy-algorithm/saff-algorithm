# 파리퇴치

T = int(input())

for tc in range(1, T+1):
    M, N = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(M)]

    max_num = 0
    for i in range(M-N+1):
        for j in range(M-N+1):
            sum_nums = 0
            for n in range(N):
                for m in range(N):
                    sum_nums += raw[n+i][m+j]
                    if max_num < sum_nums:
                        max_num = sum_nums
    
    print(f"#{tc} {max_num}")

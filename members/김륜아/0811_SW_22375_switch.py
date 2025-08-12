# 스위치 조작

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    raw1 = list(map(int, input().split()))
    raw2 = list(map(int, input().split()))
    
    count_num = 0
    
    for i in range(N):
        if raw1[i] != raw2[i]:
            for j in range(i, N):
                raw1[j] = 1 -raw1[j]
            count_num += 1
    
    print(f"#{tc} {count_num}")


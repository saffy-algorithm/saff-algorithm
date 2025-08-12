# 스위치 조작

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    count = 0
    
    # 1차원 리스트 두개에서 같은 인덱스 번호끼리 비교 ??
    for i in range(N):
        if Ai[i] == Bi[i]:
            continue
        count +=1
        for j in range(i, N):
            Ai[j] = 1 - Ai[j]
            
    
    print(f'#{tc} {count}')
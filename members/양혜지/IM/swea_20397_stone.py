# 돌 뒤집기 게임 2

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : 돌의 수 / M : 뒤집기수
    arr = list(map(int, input().split()))
    
    for _ in range(M):
        i, j = map(int, input().split())
        
        l = r = i - 1  # 투포인터 시작 위치
        for _ in range(j):
            l, r = l - 1, r + 1
            if l < 0 or r >= N:  # 범위 벗어나면 중단
                break
            if arr[l] == arr[r]:  # 좌우 값이 같으면
                arr[l] = arr[r] = arr[r] ^ 1  # 둘 다 뒤집기
    
    print(f'#{tc}', *arr)  # *: 리스트 언패킹


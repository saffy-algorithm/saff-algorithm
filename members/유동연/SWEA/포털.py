T = int(input())
for tc in range(1, 1+T):
    N = int(input()) # 방의 개수 
    P = list(map(int, input().split())) # 돌아가는 방 번호
    cnt = 1
    for i in range(1,N-1):
        retum = (i+1) - P[i]
        cnt += retum
        cnt+=2

    print(f'#{tc} {cnt}')
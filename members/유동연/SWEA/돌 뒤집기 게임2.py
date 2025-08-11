T = int(input())

for tc in range(1, T+1):
    N,M = map(int,input().split())
    stones = list(map(int, input().split()))

    dx = [-1,1]

    for _ in range(M):
        center, j = map(int, input().split())
        center-=1 #인덱스 조정

        for k in range(1, j+1): # k는 퍼져나가는
            left = center + dx[0] * k
            rightt = center + dx[1] * k

             #범위체크 ( 범위 벗어나면 안된다), 왼쪽돌과 오른쪽돌이 같은 돌이면 뒤집기
            if 0<= left and rightt <N and stones[left] == stones[rightt]:
                stones[left] = 1 - stones[left]
                stones[rightt] = 1 - stones[rightt]

    
    print(f'#{tc}', *stones)
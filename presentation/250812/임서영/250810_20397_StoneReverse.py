T = int(input())

for tc in range(T):
    # N 돌의 수 / M 뒤집기 횟수
    N, M = map(int, input().split())

    # 돌 초기상태
    stones = list(map(int, input().split()))

    for _ in range(M):
        # i번째 돌, 마주보는 돌 j개
        i, j = map(int,input().split())
        for num in range(1, j+1):
            if 0 <= i-1-num and i-1+num < N:
                if stones[i-1-num] == stones[i-1+num]:
                    stones[i-1-num] = 1 - stones[i-1-num]
                    stones[i-1+num] = 1 - stones[i-1+num]

    print(f'#{tc+1}', *stones)



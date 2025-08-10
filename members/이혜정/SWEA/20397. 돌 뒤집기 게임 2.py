T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        for k in range(1, j+1):     # j번 반복(1부터 j까지)
            if (i - 1 - k < 0) or (i - 1 + k > N-1):    # IndexError 예외처리
                break

            if stone[i - 1 - k] == stone[i - 1 + k]:    # 마주보는 돌이 같은 경우 (i는 인덱스가 아닌 '번째'를 나타내므로 i-1)
                if stone[i - 1 - k] == 0:               # 그 돌이 0이면 1으로 바꿈
                    stone[i - 1 - k], stone[i - 1 + k] = 1, 1
                else:                                   # 그 돌이 1이면 0으로 바꿈
                    stone[i - 1 - k], stone[i - 1 + k] = 0, 0


    print(f'#{t+1}', *stone)        # 출력 형식에 맞게 언패킹해서 출력

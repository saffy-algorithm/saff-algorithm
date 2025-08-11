T = int(input())

for t in range(1, T+1):
    N = int(input())
    before_switch = list(map(int, input().split()))
    after_switch = list(map(int, input().split()))
    cnt = 0

    # 같은 인덱스의 스위치가 서로 다르면 조작
    # i번 스위치 조작 후에도 같은 위치 스위치가 다른 상태이면 계속 조작
    for i in range(N):
        if before_switch[i] != after_switch[i]:
            for j in range(N - i):
                before_switch[i+j] = 1 - before_switch[i+j]     #  0 -> 1, 1 -> 0
            cnt += 1

    print(f'#{t} {cnt}')
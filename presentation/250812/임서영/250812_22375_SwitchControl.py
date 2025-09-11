T = int(input())

for tc in range(T):
    N = int(input())
    switch1 = list(map(int, input().split()))
    switch2 = list(map(int, input().split()))

    cnt = 0

    for i in range(N):
        if switch1[i] != switch2[i]:
            cnt += 1
            for j in range(i, N):
                switch1[j] = 1 - switch1[j]
        

    print(f'#{tc+1} {cnt}')
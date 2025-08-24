from collections import deque

T = 10

for tc in range(1, T+1):
    _ = int(input())
    data = list(map(int, input().split()))

    q = deque(data)
    con = True

    while con:
        for i in range(1, 6):
            num = q.popleft()
            M = num - i
            if M <= 0:
                M = 0
                q.append(M)
                con = False
                break
            q.append(M)
    

    print(f'#{tc}', *q)

        


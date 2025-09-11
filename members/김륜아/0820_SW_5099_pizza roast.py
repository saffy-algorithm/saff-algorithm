# 피자 굽기

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    oven = deque()
    for i in range(N):
        oven.append((i+1, cheese[i]))
    
    next_pizza = N

    while len(oven) > 1:
        num, chz = oven.popleft()
        chz //= 2

        if chz == 0:
            if next_pizza < M:
                oven.append((next_pizza + 1, cheese[next_pizza]))
                next_pizza += 1
        
        else:
            oven.append((num, chz))

    print(f"#{tc} {oven[0][0]}")
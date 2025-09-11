from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    q = deque()
    next_idx = 0

    while len(q) < N and next_idx < M:
        q.append((next_idx+1, cheese[next_idx]))
        next_idx += 1

    while len(q) > 1:
        idx, C = q.popleft()
        C = C // 2
        if C > 0:
            q.append((idx, C))
        
        else:
            if next_idx < M:
                q.append((next_idx+1, cheese[next_idx]))
                next_idx += 1
    
    answer = q[0][0]
    print(f'#{tc} {answer}')
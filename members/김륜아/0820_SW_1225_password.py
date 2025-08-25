 # 암호생성기

from collections import deque

T = 10

for tc in range(1, T+1):
    t = int(input())
    raw = list(map(int, input().split()))
    q = deque(raw)
    
    move_num = -1

    # 뒤로 이동하는 num이 0이면 while문 종료
    while move_num != 0:
        # 각 num이 1부터 5까지 감소하는게 한 사이클
        for i in range(1, 6):
            num = q.popleft()
            move_num = num - i
            # num이 0이 되면 for문 종료
            if (move_num) <= 0:
                move_num = 0
                q.append(move_num)
                break
            q.append(move_num)
    
    print(f"#{tc}", *q)

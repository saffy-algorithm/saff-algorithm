T = int(input())
 
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # 사람 수, 걸리는 시간, 한 번에 만드는 붕어빵 수
    customers = list(map(int, input().split()))
    customers.sort()  # 도착 시간을 오름차순 정렬
 
    possible = True
    for i in range(N):
        arrival = customers[i]            # i번째 손님 도착 시간
        made = (arrival // M) * K         # arrival 시각까지 만들어진 붕어빵 개수
        served = i + 1                    # 지금까지 도착한 손님 수
        if made < served:                 # 만들어진 붕어빵보다 손님 수가 많으면 대기 발생
            possible = False
            break
    if possible == True:
        result = 'possible'
    else:
        result = 'impossible'
    
 
    print(f'#{tc} {result}')
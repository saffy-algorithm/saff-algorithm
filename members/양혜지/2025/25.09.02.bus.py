# 전기버스

# N = 정류장 범위
# K = 한 번 충전으로 최대한 이동할 수 있는 정류장 수
# M = 충전기가 설치된 정류장 번호

# print = 최소 몇 번의 충전을 해야 종점에 도달할 수 있는가
# 종점 도착 X -> 0 출력

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int,input().split())
    charge_stop = list(map(int,input().split()))

    # 버스 정류장 개수
    bus_stop = [0]*(N+1)
 
    charge = 0 # 충전횟수
 
    # 버스 정류장에 충전기가 있으면 1로 변경
    for i in range(len(bus_stop)):
        if i in charge_stop:
            bus_stop[i] = 1
 
        # print(bus_stop)
     
    # 버스 위치
    bus_position = 0
 
    while (1):
 
        # 일단 버스 출발
        bus_position += K
 
        # 버스의 위치가 종점이거나 그 이상이면 종료
        if bus_position >= N:
            break
         
        for i in range(bus_position, bus_position-K, -1):
            if bus_stop[i] == 1:
                charge += 1
                bus_position = i
                break
        else:
            charge = 0
            break
 
    print(f'#{tc} {charge} ')
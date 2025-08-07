# 현재 위치에서 가장 멀리 갈 수 있는 위치 부터 되돌아 오면서 충전소 위치 찾기
T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    # 충전기의 위치 M개
    charges = list(map(int,input().split()))
    # 아까전에 생각 했던 대로 모양 그리기.. 충전기가 있는 역에 1 표시
    stations = [0] * (N+1)
    for i in range(M):
        # charges[i] : 충전기가 설치된 정류장 번호
        stations[charges[i]] = 1 # charges[i]번 정류장에 충전기가 있음을 표시
    # 현재 위치에서 갈 수 있는 가장 먼 곳부터 확인하고, 돌아오면서 충전소가 있는지 확인하기
    # 충전소 찾아서 충전하기 ->
    # 몇 번?이 아니라.. 목적지에 도착할 때 까지...조건 만족할 때 까지 계속 반복 >>> while
    position = 0 # 현재 위치
    cnt = 0 # 충전횟수
    # 충전소 찾는 작업을 반복
    while True:
        if position + K >= N: #position에서 충전하고 목적지 갈 수 있음
            # 더이상 충전소를 찾을 필요 없음
            break   #충전소 찾는 while문 끝내기

        #충전소 찾기 : 가장 멀리(position + K) 가서 찾아보기 >> 이전위치까지 되돌아 가면서 찾기
        for i in range(position+K, position ,-1): # i : 충전소가 있는지 확인할 정류장 번호 
            if stations[i] == 1:    # i번 정류장에는 충전기가 있음
                # 충전하기...?
                cnt += 1
                position = i
                # 충전기 찾았으니까..충전기 찾는 반복문 종료
                break
        # 반복문을 도는 동안 충전기를 못찾으면...목적지에 도착 못하는거...
        # for문이 실행하는 동안 한번도 break에 안걸리면... 실행하는 문법?
        else:
            cnt = 0
            break #충전기 찾아서 이동하는 반복 종료

    print(f'#{tc} {cnt}')
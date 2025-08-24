# 2에서 출발
# r=0 시 종료
# 상좌우만 봐
# 계속 올라가 내려가지마
# 옆에 0이 없으면 꺾어 ..?

T = 10
 
for tc in range(1,T+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
 
    # 위, 왼쪽, 오른쪽
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    move = 0
 
    # 도착 지점 인덱스 찾기 arr[99][end]
    for i in range(100):
        if arr[99][i] == 2:
            end = i
    # end = arr[99].index(2)
    y = 99
    x = end
 
    while y > 0:
        # 왼쪽 사다리 확인
        if x > 0 and arr[y][x - 1] == 1:
            move = 1 # 방향을 '왼쪽'으로 설정
            # 사다리가 끝날 때까지 왼쪽으로 이동
            while x > 0 and arr[y][x - 1] == 1:
                x += dc[move] # 열(x)만 변경
             
        # 오른쪽 사다리 확인
        elif x < 99 and arr[y][x + 1] == 1:
            move = 2 # 방향을 '오른쪽'으로 설정
            # 사다리가 끝날 때까지 오른쪽으로 이동
            while x < 99 and arr[y][x + 1] == 1:
                x += dc[move] # 열(x)만 변경
             
        # 좌우에 사다리가 없거나, 옆 이동이 끝났으면 위로 한 칸 이동
        y += dr[0]
 
 
    print(f'#{tc} {x}')
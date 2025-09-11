from pprint import pprint

# 정지, 상하우좌
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
    M, A = map(int,input().split()) # M: 이동 시간, A: BC의 개수
    info_a = list(map(int,input().split())) # 사용자 A의 이동정보
    info_b = list(map(int,input().split())) # 사용자 B의 이동정보
    BC_info = [] # 충전소의 정보를 담을거임

    for _ in range(A):
        # (x,y) AP 1/2의 정보, c = 충전 범위량 p = 충전량
        x, y, c, p = map(int,input().split())
        arr = [[0]*10 for _ in range(10)]
    for k in range(1,A+1):
        x, y = 00


    for i in range(10):
        for j in range(10):
            if abs(x - i) + abs(y - j) <= c:
                arr[i][j] = [0]
                arr[i][j].append(k)    


# 2차원 배열 빈 지도를 만들어서 값을 넣고  . . ?
# 시간변수 따로 M이 이동시간
# A만큼 어펜드하고
# 1, M+1만큼 돌아 ..?

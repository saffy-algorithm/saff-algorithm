from pprint import pprint

# 상하우좌
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
    M, A = map(int,input().split()) # M: 이동 시간, A: BC의 개수
    info_a = list(map(int,input().split())) # 사용자 A의 이동정보
    info_b = list(map(int,input().split())) # 사용자 B의 이동정보
    # (x,y) AP 1/2의 정보, c = 충전 범위량 p = 충전량
    x, y, c, p = map(int,input().split())

    jido = [[0]*10 for _ in range(10)]
    pprint(jido)
    


# info_a/b를 그냥 리스트로 받아도되능가
# 2차원 배열 빈 지도를 만들어서 값을 넣고  . . ?
# 시간변수 따로 M이 이동시간

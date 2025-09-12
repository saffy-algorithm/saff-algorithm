dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 1. 종료 조건 : 숫자 7자리일 때 종료
# 2. 가지의 수 : 4개 (상하좌우)
def recur(y, x, number):
    if len(number) == 7 : # 7자리면 종료

        # set에 추가 
        # 글로벌 왜 안했냐면 -> 주소값을 전역변수에 가지고 있음
        # method 호출 했기 때문에 ㄱㅊ
        result.add(number) 
        return
    
    for i in range(4): # 상하좌우
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 밖이면 다음 방향 확인 (continue)
        if ny < 0 or ny >= 4 or nx < 0 or nx >=4:
            continue
        
        # 무조건 중복되게 상하좌우 이동만하면 됨
        # 다음 위치로 이동
        # 다음으로 넘어갈 때 누적해줘야하는 값이 무엇이냐
        recur(ny, nx, number + matrix[ny][nx]) 


T = int(input())
for tc in range(1, T+1):
    matrix = [input().split() for _ in range(4)]
    result = set()

#     # 7자리 만드는 코드
#     # 4 * 4가 모두 출발점이 될 수 있다
#     for sy in range(4):
#         for sx in range(4):
#             recur(sy, sx, matrix[sy][sx])

#     print(f'#{tc} {len(result)}')

# BFS 로 접근하는 방법
# - 재귀호출이 누적되는 값을 파라미터로 받았다면
# - queue 에 누적되는 값을 같이 추가

# 접근 법
# - 시작 지점 : 전체 다 보아야 한다.
# - 재귀 돌리면서(상하좌우 이동) 숫자를 붙인다
# - 숫자가 7자리가 되면, set에 넣는다. (중복제거)
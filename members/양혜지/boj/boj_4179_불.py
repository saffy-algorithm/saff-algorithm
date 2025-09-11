# 상하우좌
dr = [-1, 1, 0, 0]
dc = [0, 0, 1,-1]

R, C = map(int,input().split())
miro = [list(map(str,input())) for _ in range(R)]
cnt = 1

# 불이랑 사람중에 누가 먼저 이동 ? 불이 먼저 ?
# BFS가 두개 ?
# 두개가 같이 이동
# 
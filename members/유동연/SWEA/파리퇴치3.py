# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # d1 = [0, 1, 0, -1]   # 상, 하, 좌, 우를 위한 코드
#     # d2 = [1, 0, -1, 0]   # 상, 하, 좌, 우를 위한 코드
#     # d3 = [1, 1, -1, -1]  # 대각선을 위한 코드
#     # d4 = [1, -1, -1, 1]  # 대각선을 위한 코드
#     d1 = [(0,1),(1,0),(0,-1),(-1,0)]   # 상, 하, 좌, 우를 위한 코드
#     d2 = [(1,1), (1,-1), (-1,-1), (-1,1)] # 대각선을 위한 코드
    
#     max_kill = 0    #죽인 버그들 누적하기 전 값. int(-float?)이것도 가능하다고 봄

#     for i in range(N):
#         for j in range(N):
#             plus = arr[i][j] 
#             for direct in range(4): # 4를 한 이유? d1, d2의 0, 1, 2, 3 인덱스를 순회하기 위해
#                 for c in range(1, M):  # c는 1, 3 즉, 자신으로부터 2칸씩 더하기 위해
#                     ni, nj = i+d1[direct]*c, j+d2[direct]*c  # + 에프킬라 모양
#                     if 0<=ni<N and 0<=nj<N:   # 초과하는 공간 무시!
#                         plus+= arr[ni][nj]
#             max_kill = max(max_kill, plus)

#     for r in range(N):
#         for c in range(N):
#             plus = arr[r][c] 
#             for direct in range(4):
#                 for w in range(1, M):
#                     nr, nc = r+d3[direct]*w, c+d4[direct]*w
#                     if 0<=nr<N and 0<=nc<N:
#                         plus+= arr[nr][nc]
#             max_kill = max(max_kill, plus)





#     print(f'#{tc+1} {max_kill}')



    #+ 
# def plus_spray(x,y):
#     delta = [(-1,0), (0,-1), (1,0), (0,1)]
#     total = arr[x][y] #각 좌표 합(누적)
 
#     for dx, dy in delta:
#         for i in range(1, M):
#             arr_x,arr_y = x+dx*i, y+dy*i
#             if 0 <= arr_x <N and 0<= arr_y <N:
#                 total += arr[arr_x][arr_y]
#     return total
 
# #x
# def cross_spray(x,y):
#     delta = [(1,1),(1,-1),(-1,1),(-1,-1)]
#     total = arr[x][y] #각 좌표 합(누적)
 
#     for dx, dy in delta:
#         for i in range(1, M):
#             arr_x,arr_y = x+dx*i, y+dy*i
#             if 0<= arr_x<N and 0<= arr_y <N:
#                 total += arr[arr_x][arr_y]
#     return total
 
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
 
#     answer = 0
#     for i in range(N):
#         for j in range(N):
#             answer = max(answer, plus_spray(i,j),cross_spray(i,j))
#     print(f'#{tc+1} {answer}')
    
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    d_p = [(0,1),(1,0),(0,-1),(-1,0)]
    d_x = [(1,1),(1,-1),(-1,-1), (-1,1)]
    
    max_kill = 0
    for i in range(N):
        for j in range(N):
            plus = arr[i][j]
            for direct in range(4):
                for p in range(1, M):
                    ni, nj = i+d_p[direct][0]*p, j+d_p[direct][1]*p
                    if 0<=ni<N and 0<=nj<N:
                        plus += arr[ni][nj]
            max_kill = max(plus, max_kill)

    for i in range(N):
        for j in range(N):
            plus = arr[i][j]
            for direct in range(4):
                for x in range(1, M):
                    ni, nj = i+d_x[direct][0]*x, j+d_x[direct][1]*x
                    if 0<=ni<N and 0<=nj<N:
                        plus += arr[ni][nj]
            max_kill = max(plus, max_kill)
    print(max_kill)
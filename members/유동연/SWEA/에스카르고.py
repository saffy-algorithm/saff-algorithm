# T = int(input())
# d = [(0,1), (1,0), (0,-1), (-1,0)]


# for tc in range(1, 1+T):
#     N = int(input())
#     arr = [[0]*N for _ in range(N)]
#     dist = 0
#     r, c =0, 0
#     for n in range(1, N*N+1):
#         arr[r][c] = N
#         r+= d*[dist]
#         c+= d*[dist]
#     if r<0 or c <0 or r>=N or c>= N or arr[r][c]!= 0:
#         r-= d[dist]
#         c-= d[dist]
#         dist = (1+dist)%4

#         r+= d[dist]
#         c+= d[dist]
#     print(f'#{tc}')

#     for row in arr:
#         print(*row)
T = int(input())
d = [(0,1), (1,0), (0,-1), (-1,0)]

for tc in range(1, 1+T):
    N= int(input())
    arr = [[0]*N for _ in range(N)]
    r, c = 0, 0
    dist = 0
    for i in range(1,N*N+1):
        arr[r][c] = i
        r += d[dist][0]
        c += d[dist][1]
        if r<0 or c<0 or r>=N or c>=N or arr[r][c] != 0:
            r -= d[dist][0]
            c -= d[dist][1]
            dist = ((1+dist)%4)

            r += d[dist][0]
            c += d[dist][1]
    print(f'#{tc}')
    for row in arr:
        print(*row)


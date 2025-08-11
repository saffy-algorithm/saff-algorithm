T = int(input())
d1 = [(0,1), (1,0), (0,-1), (-1,0)]


for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    numbers = 0
    for i in range(N):
        for j in range(N):
            count = 0
            count += arr[i][j]
            for d in range(4):
                for k in range(1,N):
                    nr = i + d1[d][0] *k
                    nc = j + d1[d][1] *k  
                    if 0<=nr<N and 0<=nc<N:
                        count+= arr[nr][nc]
            
                if numbers<count:
                    numbers=count
    print(f'#{tc} {numbers}')
                    



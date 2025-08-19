T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    arr = [[1] * (i+1) for i in range(N)]  # 삼각형 배열 1만
 
    # 가운데 빼고 
    for i in range(2, N):
        for j in range(1, i):   # 양끝이 아니면
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j] # 위에 두개 더해서 밑에
 
 
    print(f'#{tc}')
    for i in arr:
        print(*i)
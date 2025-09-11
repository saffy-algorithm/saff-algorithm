# 어디에 단어가 들어갈 수 있을까

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    cnt_len = 0 # 1을 만나면 누적
    cnt_a = 0 # 가로에서 K랑 같은 단어 만나면 누적
    cnt_b = 0 # 세로에서 K랑 같은 단어 만나면 누적

    # 가로행 검사
    for i in range(N):
        cnt_len = 0
        for j in range(N):
            # 행을 돌면서 1을 만나면 len 에 누적
            
            if arr[i][j] == 1:
                cnt_len += 1
            else:
                cnt_len = 0

            if cnt_len == K:
                cnt_a += 1
                cnt_len = 0
            
        
            
            # len이랑 K와 같아질 때까지 돌아
            # 언제 멈출지를 생각
            # 1. 배열이 끝나고, K개랑 같아졌을 때
                # cnt_a에 누적시키고 len을 초기화
            while cnt_len > K:
                if cnt_len == K and j == N-1:
                    cnt_a += 1
                    cnt_len = 0

                # 2. K개랑 같아졌고, 뒤에 0이 있을 때
                # cnt_a에 누적시키고 len을 초기화
                else:
                    cnt_len == K and arr[i][j]
                    cnt_a += 1
                    cnt_len = 0

    # 세로열 검사
    for j in range(N):
        for i in range(N):
            # 행을 돌면서 1을 만나면 len 에 누적
            if arr[i][j] == 1:
                cnt_len += 1
            # len이랑 K와 같아질 때까지 돌아
            # 언제 멈출지를 생각
            # 1. 배열이 끝나고, K개랑 같아졌을 때
                # cnt_a에 누적시키고 len을 초기화
            
            while cnt_len > K:
                if cnt_len == K and i == N-1:
                    cnt_b += 1
                    cnt_len = 0

                # 2. K개랑 같아졌고, 뒤에 0이 있을 때
                # cnt_a에 누적시키고 len을 초기화
                else:
                    cnt_len == K and arr[i][j]
                    cnt_b += 1
                    cnt_len = 0

    print(f'#{tc} {cnt_a+cnt_b}')


            # if arr[i][j]==0 and i==N-1:
            #     if K== cnt_len:
            #         cnt_b +=1


        # 행 고르기
        for r in range(N):
            c = 0
            count = 0 
            while c < N:
                if arr[r][c] == 1:
                    count += 1
                else:
                    count = 0
                c += 1
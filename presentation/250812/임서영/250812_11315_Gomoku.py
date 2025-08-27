T = int(input())

for tc in range(1, T+1):
    N = int(input())
    omog = [input() for _ in range(N)]
    ans = 'NO'

    # 직선
    for i in range(N):
        # 가로 검사
        if 'ooooo' in omog[i]:
                ans = 'YES'
        for j in range(N):
            # 세로 검사
            col = ''
            # 세로를 한 문자열로 저장
            for r in range(N):
                col += omog[r][j]
            if 'ooooo' in col:
                ans = 'YES'
            
            # 대각선
            cnt = 0
            rev_cnt = 0
            for d in range(N):
                if i+d<N:
                #우하향
                    if j+d<N and omog[i+d][j+d] == 'o':
                        cnt += 1
                    else:
                        if cnt >= 5 or rev_cnt >= 5:
                            ans = 'YES'
                            break
                        cnt = 0
                #좌하향
                    if 0<=j-d and omog[i+d][j-d] == 'o':
                        rev_cnt += 1
                    else:
                        if cnt >= 5 or rev_cnt >= 5:
                            ans = 'YES'
                            break
                        rev_cnt = 0
                else:
                    if cnt >= 5 or rev_cnt >= 5:
                        ans = 'YES'
            if cnt >= 5 or rev_cnt >= 5:
                ans = 'YES'
                

    print(f'#{tc} {ans}')
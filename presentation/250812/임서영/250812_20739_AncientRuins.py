T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    anc = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    cnt = 0

    for i in range(N):
        for j in range(M):
            if anc[i][j] == 1:
                cnt += 1
            else:
                if cnt >= 2 and cnt > max_cnt: # 1X2이상이어야 한다는 조건 참고
                    max_cnt = cnt
                cnt = 0
        if cnt >= 2 and cnt > max_cnt:
                max_cnt = cnt
        cnt = 0

    for j in range(M):
        for i in range(N):
            if anc[i][j] == 1:
                cnt += 1
            else:
                if cnt >= 2 and cnt > max_cnt: # 1X2이상이어야 한다는 조건 참고
                    max_cnt = cnt
                cnt = 0
        if cnt >= 2 and cnt > max_cnt:
                max_cnt = cnt
        cnt = 0

    print(f'#{tc+1} {max_cnt}')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    omog = [input().strip() for _ in range(N)]

    ans = 'NO'
    dirs = [(0, 1), (1, 0), (1, 1), (1, -1)]  # →, ↓, ↘, ↙

    for i in range(N):
        if ans == 'YES':
            break
        for j in range(N):
            if ans == 'YES':
                break
            if omog[i][j] != 'o':
                continue

            for dx, dy in dirs:
                # 이 칸이 해당 방향 연속구간의 '시작'인지 확인
                pi, pj = i - dx, j - dy
                if 0 <= pi < N and 0 <= pj < N and omog[pi][pj] == 'o':
                    continue  # 시작점이 아니면 스킵

                # 시작점이면 앞으로 쭉 세기
                x, y = i, j
                cnt = 0
                while 0 <= x < N and 0 <= y < N and omog[x][y] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        ans = 'YES'
                        break
                    x += dx
                    y += dy
                if ans == 'YES':
                    break

    print(f'#{tc} {ans}')

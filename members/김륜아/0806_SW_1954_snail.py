# 달팽이 숫자

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    di = [0, +1, 0, -1]
    dj = [+1, 0, -1, 0]

    i, j = 0, 0
    delta = 0

    for num in range(1, N**2 + 1):
        snail[i][j] = num

        ni = i + di[delta]
        nj = j + dj[delta]

        if 0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0:
            i, j = ni, nj

        else:
            delta = (delta + 1) % 4
            i += di[delta]
            j += dj[delta]
    
    print(f"#{tc}")
    for Snail in snail:
        print(*Snail)

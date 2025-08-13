# 오목

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    switch = 'NO'
 
    for i in range(N):
        x_count = 0
        for j in range(N):
            if arr[i][j] == "o":
                x_count += 1
            else:
                if x_count >= 5:
                    switch = 'YES'
                x_count = 0
            if j == N - 1:
                if x_count >= 5:
                    switch = 'YES'
    for j in range(N):
        y_count = 0
        for i in range(N):
            if arr[i][j] == "o":
                y_count += 1
            else:
                if y_count >= 5:
                    switch = 'YES'
                y_count = 0
            if i == N - 1:
                if y_count >= 5:
                    switch = 'YES'
    for i in range(N):
        for j in range(N):
            if i + 4 < N and j + 4 < N:
                if all(arr[i + k][j + k] == 'o' for k in range(5)):
                    switch = 'YES'
            if i - 4 >= 0 and j + 4 < N:
                if all(arr[i - k][j + k] == 'o' for k in range(5)):
                    switch = 'YES'
    print(f'#{tc} {switch}')
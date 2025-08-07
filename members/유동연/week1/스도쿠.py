T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    flag = False  # 스도쿠 오류 여부 저장

    # 1. 행 검사
    for i in range(9):
        visited = [0] * 10
        for j in range(9):
            if visited[arr[i][j]]:
                flag = True
                break
            visited[arr[i][j]] = 1
        if flag:
            break

    # 2. 열 검사
    if not flag:
        for j in range(9):
            visited = [0] * 10
            for i in range(9):
                if visited[arr[i][j]]:
                    flag = True
                    break
                visited[arr[i][j]] = 1
            if flag:
                break
    
    # 3x3 검사!
    if not flag:
        for k in range(9):
            visited = [0]*10
            start_r = 3*(k//3)
            start_c = 3*(k%3)
            for i in range(3):
                for j in range(3):
                    txt = arr[start_r+i][start_c+j]
                    if visited[txt]:
                        flag =True
                        break
                    visited[txt] = 1
            if flag:
                break

                    
    if not flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

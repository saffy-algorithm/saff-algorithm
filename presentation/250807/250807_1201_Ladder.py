for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]


    #끝나는 지점이 2인 좌표 찾기(여기서 시작)
    for j in range(100):
        if data[99][j] == 2:
            x = 99
            y = j
            break #불필요한 계산 제거


    #아래서부터 이어지게 올라가기
    while x > 0 :
        if y > 0 and data[x][y-1] == 1:
            while y > 0 and data[x][y-1] == 1:
                y -= 1
            x -= 1

        elif y < 99 and data[x][y+1] == 1:
            while y < 99 and data[y][y+1] == 1:
                y += 1
            x -= 1
        else:
            x -= 1

    print(f'#{tc} {y}')
# 스도쿠

T = int(input())

for tc in range (1, T+1):
    sdk_1 = [list(map(int, input().split())) for _ in range(9)]
    
    answer1 = 1
    answer2 = 1
    answer3 = 1

    right = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in range(9):
        if sorted(sdk_1[i]) != right:
            answer1 = 0
            break
   
    sdk_2 = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            sdk_2[i][j] = sdk_1[j][i]
    
    for i in range(9):
        if sorted(sdk_2[i]) != right:
            answer1 = 0
            break
    
    sdk_3 = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            for n in range(3):
                for m in range(3):
                    box.append(sdk_1[i + n][j + m])
            sdk_3.append(box)

    for i in range(9):
        if sorted(sdk_3[i]) != right:
            answer1 = 0
            break

    if answer1 + answer2 + answer3 == 3:
        answer = 1
    else:
        answer = 0

    print(f"#{tc} {answer}")

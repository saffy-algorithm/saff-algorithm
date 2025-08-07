# Ladder1

for tc in range(1, 11):
    T = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]

    X_num = 0
    for X in range(0, 100):
        if ladder_list[99][X] == 2:
            X_num = X
            break

    i, j = 99, X
    
    for _ in range(100):

        if j < 99 and ladder_list[i][j+1] == 1:
            while j < 99 and ladder_list[i][j+1] == 1:
                i, j = i, (j+1)
            i, j = (i-1), (j)
        
        elif j > 0 and ladder_list[i][j-1] == 1:
            while j > 0 and ladder_list[i][j-1] == 1:
                i, j = i, (j-1)
            i, j = (i-1), (j)

        else:
            i, j = (i-1), (j)

                

    print(f"#{tc} {j}")

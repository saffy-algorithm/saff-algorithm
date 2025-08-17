for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
 
    row_lst = []
    col_lst = []
    diag_lst = []
    result = 0
 
    for i in range(100):
        row = 0
        col = 0
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
         
        row_lst.append(row)
        col_lst.append(col)
         
    diag1 = 0
    diag2 = 0
    for r in range(100):
        diag1 += arr[r][r]
        diag2 += arr[r][99-r]
 
    diag_lst.append(diag1)
    diag_lst.append(diag2)
 
    result = max(max(row_lst), max(col_lst), max(diag_lst))
 
    print(f'#{T} {result}')
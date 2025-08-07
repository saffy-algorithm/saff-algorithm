def check_sudoku(sudoku):
    #row 확인

    for row in sudoku:
        if len(set(row)) != 9:
            return 0


    #colum 확인
    for col in range(9):
        col_list = []
        for row in range(9):
            col_list.append(sudoku[row][col])
        if len(set(col_list)) != 9:
            return 0

    #3X3 확인
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            three_list = []
            for x in range(3):
                for y in range(3):
                    three_list.append(sudoku[box_row + x][box_col + y])
            if len(set(three_list)) != 9:
                    return 0


    return 1



N = int(input())

for num in range(N):
    sudoku = []
    for _ in range(9):
        row = list(map(int, input().split()))
        sudoku.append(row)
    result = check_sudoku(sudoku)
    print(f'#{num + 1} {result}')
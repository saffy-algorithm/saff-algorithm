# 스도쿠 검증
# 가로 세로 3X3 중복 안됨

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    
    # 가로 세로 검사
    for i in range(9):
        for j in range(9):
            # 행 검사
            row_arr = set(arr[i])
            col_arr = set
            
            if len(set(row_arr))!=9 or len(col_arr)! =9:
    
    



    print(f'#{tc} {}')
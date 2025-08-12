# 회문인지 어떻게 확인 ?
# 반으로 갈라서 ../?

for tc in range(1, 11):
    N = 8
    K = int(input()) # 찾아야 하는 회문의 길이
    middle = K // 2
    arr = [list(input()) for _ in range(N)]
    count = 0
    
    for i in range(N):
        for j in range(N - K + 1):
            arr_row = arr[i][j:j + K] # 슬라이싱 변수 선언
            for m in range(K):
                if arr_row[m] == arr_row[-(m + 1)]:
                    pass
                else:
                    break
            else:
                count += 1
      
    for j in range(N):
        for i in range(N - K + 1):
            arr_col = []
            for k in range(K):
                arr_col.append(arr[i + k][j])
            for m in range(K):
                if arr_col[m] == arr_col[-(m + 1)]:
                    pass
                else:
                    break
            else:
                count += 1
                  
    print(f'#{tc} {count}')
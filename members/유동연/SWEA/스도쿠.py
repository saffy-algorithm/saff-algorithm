# T = int(input())
# for tc in range(1,1+T):
#     arr = [list(map(int, input().split())) for _ in range(9)]

#     flag = False #문제 없는 상태()
#     for i in range(9):
#         visited = [0]*10
#         for j in range(9):
#             # arr[i][j] 이미 체크됨
#             if visited[arr[i][j]]:
#                 flag = True #flag가 True이면 스도쿠 오류 따라서 0을 출력
#                 break
        
#             # arr[i][j] 아직 체크 안 됨
#             else:
#                 visited[arr[i][j]] = 1
        
#         if flag:
#             break

#         # i행 순회 완료 > 중복 체크
#     if not flag:
#         for j in range(9):
#             visited = [0]*10
#             for i in range(9):
#                 if visited[arr[i][j]]:
#                     flag = True
#                     break
                
#                 visited[arr[i][j]] =1
#             if flag:
#                 break
#     if not flag:
#         for si in range(0, 9, 3):       # 시작 행 인덱스: 0, 3, 6
#             for sj in range(0, 9, 3):   # 시작 열 인덱스: 0, 3, 6
#                 visited = [0]*10        # 1~9 숫자 중복 체크용
#                 for i in range(3):      # 3행
#                     for j in range(3):  # 3열
#                         num = arr[si+i][sj+j]
#                         if visited[num]:
#                             flag = True
#                             break
#                         visited[num] = 1
#                 if flag:
#                     break
#             if flag:
#                 break
#         if flag:
#             break

#     print(f'#{tc} {0 if flag else 1}')     

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

    # 3. 3x3 박스 검사
    if not flag:
        for si in range(0, 9, 3):
            for sj in range(0, 9, 3):
                visited = [0] * 10
                for i in range(3):
                    for j in range(3):
                        num = arr[si + i][sj + j]
                        if visited[num]:
                            flag = True
                            break
                        visited[num] = 1
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break
    if flag == False:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')



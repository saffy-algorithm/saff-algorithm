# T = 10
# for tc in range(1, 1+T):
#     N = int(input())
#     str_lst = [list(input()) for _ in range(8)]
#     ans = 0

#     for i in range(8):
#         for j in range(8):
#             for x in range(8-N+1):
#                 new_arr = str_lst[i][x:x+N]
#                 if new_arr == new_arr[::-1]:
#                     ans+=1

    
#     for col in zip(*str_lst):
    
#         for x in range(8-N+1):
#             new_arr = col[i][x:x+N]
#             if new_arr == new_arr[::-1]:
#                 ans+=1
#     print(f'#{tc} {ans}')
        

                
        



T = 10
for tc in range(1, 1+T):
    N = int(input())
    str_lst = [list(input()) for _ in range(8)]
    ans = 0

    # 가로 회문 검사
    for row in str_lst:
        for x in range(8-N+1):
            new_arr = row[x:x+N]
            if new_arr == new_arr[::-1]:
                ans += 1
    
    # 세로 회문 검사
    for col in zip(*str_lst):
        for x in range(8-N+1):
            new_arr = col[x:x+N]
            if new_arr == new_arr[::-1]:
                ans += 1

    print(f'#{tc} {ans}')
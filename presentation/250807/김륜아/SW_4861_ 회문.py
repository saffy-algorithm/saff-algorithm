# 회문

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 문자 리스트로 받기
    str_raw = [input() for _ in range(N)]
    
    # 문자 리스트 전치 (세로 회문 점검 위함)
    raw_vertical_list = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            raw_vertical_list[i][j] = str_raw[j][i]
    str_raw_vertical = []
    for idx in range(N):
         str_raw_vertical.append(''.join(raw_vertical_list[idx]))

    answer = ''
    # 가로 & 세로 회문
    answer = ''
    for line in str_raw + str_raw_vertical:
        for j_idx in range(N-M+1):
            check = line[j_idx:j_idx+M]
            if check == check[::-1]:
                answer = check
                break
        if answer:
            break
        
    print(f"#{tc} {answer}")




    for i in range(N):
        for j in range(N-M+1):
            if M % 2 == 1:
                if raw_list[i][j:j+M//2] == raw_list[i][j+M-1:j+(M//2):-1]:
                    print(f"#{tc} {raw_list[i][j:j+M]}")
                    break
                    
                
                if str_raw_vertical[i][j:j+M//2] == str_raw_vertical[i][j+M-1:j+(M//2):-1]:
                    print(f"#{tc} {str_raw_vertical[i][j:j+M]}")
                    break
            else:
                if raw_list[i][j:j+M//2] == raw_list[i][j+M-1:j+(M//2)-1:-1]:
                    print(f"#{tc} {raw_list[i][j:j+M]}")
                    break
                    
                
                if str_raw_vertical[i][j:j+M//2] == str_raw_vertical[i][j+M-1:j+(M//2)-1:-1]:
                    print(f"#{tc} {str_raw_vertical[i][j:j+M]}")
                    break
                    
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    raw_list = [input() for _ in range(N)]

    # 1) 전치하여 세로 문자열 리스트 만들기
    transposed_list = [''.join(raw_list[j][i] for j in range(N)) for i in range(N)]

    answer = ''
    # 2) 가로와 세로 모두 검사
    for line in raw_list + transposed_list:  # 가로 줄들 + 세로 줄들
        for j_idx in range(N - M + 1):
            substring = line[j_idx:j_idx + M]
            if substring == substring[::-1]:  # 회문 검사
                answer = substring
                break
        if answer:
            break

    print(f"#{tc} {answer}")

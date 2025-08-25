#   정곤이의 단조 증가하는 수

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    raw = list(map(int, input().split()))
    
    max_answer = -1

    for i in range(N-1):

        for i_next in range(i+1, N):
            num = raw[i] * raw[i_next]

            # num값이 max_answer보다 작으면 pass
            if max_answer >= num:
                continue
            
            # 숫자를 문자로
            s_num = str(num)

            # num 자릿수가 1이면 단조 OK
            if len(s_num) == 1:
                check = True

            elif len(s_num) > 1:
                check = True
                for idx in range(len(s_num) - 1):
                    if (s_num)[idx] > (s_num)[idx + 1]:
                        check = False
                        break
                
            if check:
                max_answer = max(max_answer, num)

    print(f"#{tc} {max_answer}")


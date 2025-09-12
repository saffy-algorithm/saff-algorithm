T = int(input())
 
for tc in range(T):
    N = int(input())
    num = list(map(int, input()))
 
    cnt = [0] * 10
 
    for i in num:
        cnt[i] += 1 #인덱스 값 = 숫자
 
    max_cnt = 0
    max_num = 0
 
    for digit in range(10):
        if cnt[digit] >= max_cnt:
            max_cnt = cnt[digit]
            max_num = digit
 
        
    print(f'#{tc+1} {max_num} {max_cnt}')
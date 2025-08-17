T = int(input())
 
for tc in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
 
    count = 0
    word_len = 0
 
 
    for i in range(N):
        word_len = 0
        for j in range(N):
            if puzzle[i][j] == 1: # 1이면 길이 세기
                word_len += 1
            else: # else = 0을 만났을 때
                if word_len == K:
                    count += 1
                word_len = 0 
        if word_len == K: # 마지막에 IF문에 걸린 다음에 나왔을 때 K라면!
            count += 1
 
    for j in range(N):
        word_len = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                word_len += 1
            else:
                if word_len == K:
                    count += 1
                word_len = 0
        if word_len == K:
            count += 1
 
 
 
    print(f'#{tc+1} {count}')
for tc in range(1, 11):
    N = int(input())
    words = [input() for _ in range(8)]

    result = 0

    for r in range(8):
        for c in range(8 - N + 1):
            for i in range(N//2):
                if words[r][c+i] != words[r][c+N-1-i]:
                    break
            else:
                result += 1

            for i in range(N//2):    
                if words[c+i][r] != words[c+N-1-i][r]:
                    break
            else:
                result += 1

    print(f'#{tc} {result}')
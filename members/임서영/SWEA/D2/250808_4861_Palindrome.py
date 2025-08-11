T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]

    palindrome = ''

    for r in words:
        for c in range(N - M + 1):
            check = r[c:c+M]
            if check == check[::-1]:
                palindrome = check
                break

    if palindrome == '':
        for r in zip(*words):
            for c in range(N - M + 1):
                check = r[c:c+M]
                if check == check[::-1]:
                    palindrome = check
                    break


    result = ''.join(palindrome)

    print(f'#{tc+1} {result}')
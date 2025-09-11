T = int(input())

for tc in range(1, T+1):

    arr = list(input().split('.'))
    ans = ''
    word = []

    for i in arr:
        word.append(i[::-1])
    
    ans = '.'.join(word)
    

    print(f'#{tc} {ans}')
    
    
# 3
# I.evol.YFASS
# ,olleH.!dlroW.321
# a.ba..cba
T = int(input())

    
for tc in range(T):
    
    flag = False

    N,M,K = map(int,input().split())
    
    ppl = list(map(int,input().split()))
    sort_ppl = sorted(ppl)


    count = 0
    for i in sort_ppl:

        make = i // M * K #이 사람이 올떄 내가 만들수있는 붕어빵 수
        count += 1 #사람 수

        if make < count: #만든게 사람보다 적으면 바로 impossible
            print(f'#{tc+1} Impossible')
            flag = True
            break

    else:
        print(f'#{tc+1} Possible')


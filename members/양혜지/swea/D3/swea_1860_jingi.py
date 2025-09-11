# 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    people = list(map(int,input().split()))
    people.sort()
    fish = 0
    
    # i = 현재 초
    switch = "Possible"

    for i in range(people[-1]+1): 
        # M초마다 K개만큼 붕어빵 개수를 추가한다
        if i % M == 0 and i !=0 : # 0초에도 사람이 오므로 > 0이 아닌 경우만 고려
            fish +=K
            
        # 현재 시간에 손님이 오는지
        if i in people:
            nums = people.count(i) # 몇명이 오는지
            
            # 손님수가 붕어빵보다 많으면 불가능
            if nums > fish:
                switch = "Impossible"
            
            # 그게 아니면 붕어에서 손님수만큼 차감     
            else:
                fish-=nums
        
    print(f'#{tc} {switch}')
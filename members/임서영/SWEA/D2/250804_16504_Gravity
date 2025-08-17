T = int(input())
 
for tc in range(T):
    N = int(input())
    test_list = list(map(int, input().split()))
 
    drop = 0 # 각 낙차
    max_drop = 0 # 낙차 최대값
 
    for i in range(len(test_list) - 1):
        drop = 0
        for j in test_list[i:]:  
            if test_list[i] > j:
                drop += 1
 
        if drop > max_drop:
            max_drop = drop
 
 
    print(f'#{tc+1} {max_drop}')
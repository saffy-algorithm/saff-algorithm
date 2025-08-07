T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    A_l = 1
    A_r = P
    A_c = int((A_l + A_r)/2)
    B_l = 1
    B_r = P
    B_c = int((B_l + B_r)/2)
    A_count = 0
    B_count = 0
    
    while A_c != Pa:
        A_count += 1
        if A_c < Pa:
            A_l = A_c
            A_c = int((A_l + A_r)/2) # A 센터가 옮겨짐
        elif A_c > Pa:
            A_r = A_c
            A_c = int((A_l + A_r)/2)
            
    while B_c != Pb:
        B_count += 1
        if B_c < Pb:
            B_l = B_c
            B_c = int((B_l + B_r)/2)
        elif B_c > Pb:
            B_r = B_c
            B_c = int((B_l + B_r)/2)
            
    if A_count < B_count:
        print(f'#{tc} A')
    elif A_count > B_count:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')    
            
    
    

            
            

            
            




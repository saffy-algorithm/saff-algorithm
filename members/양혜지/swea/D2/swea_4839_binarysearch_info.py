T = int(input()) # 테스트 케이스 개수 입력 받음

for tc in range(1, T+1): # T만큼 반복
    P, Pa, Pb = map(int, input().split()) # 전체 쪽수, 찾을 쪽 번호 입력 받음
    A_l = 1
    A_r = P
    A_c = int((A_l + A_r)/2) # A의 센터
    B_l = 1
    B_r = P
    B_c = int((B_l + B_r)/2) # B의 센터
    A_count = 0 # 반복문 돌면서 몇번만에 정답 쪽수 찾는지 세어줄 변수
    B_count = 0
    
    while A_c != Pa: # A센터랑 찾을 쪽수가 같으면 반복문 멈추게 할거다
        A_count += 1 # 돌때마다 +1씩
        if A_c < Pa: # A센터보다 Pa가 크면
            A_l = A_c # A왼쪽을 A센터로 옮겨준다
            A_c = int((A_l + A_r)/2) # A센터가 옮겨졌음
        elif A_c > Pa: # A센터보다 Pa가 작으면
            A_r = A_c # A오른쪽을 A센터로 옮겨준다
            A_c = int((A_l + A_r)/2) # A센터가 옮겨졌음
            
    while B_c != Pb: # A와 B 동일
        B_count += 1
        if B_c < Pb:
            B_l = B_c
            B_c = int((B_l + B_r)/2)
        elif B_c > Pb:
            B_r = B_c
            B_c = int((B_l + B_r)/2)
            
    if A_count < B_count: # 승부 확인할거임 A횟수보다 B횟수가 크면
        print(f'#{tc} A') # A 횟수 출력 -> 이긴사람
    elif A_count > B_count: # B횟수보다 A횟수가 크면
        print(f'#{tc} B') # B 횟수 출력 -> 이긴사람
    else:
        print(f'#{tc} 0') # 비기면 0 출력
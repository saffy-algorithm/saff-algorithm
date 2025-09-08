# 행열 바뀜
# 1부터 시작

# 제상우하좌 : 행렬이 바뀌어있으니까
dr = [0, 0, 1, 0, -1]
dc = [0, -1, 0, 1, 0]

T = int(input())
for tc in range(1, T+1):
    N, BC_count = map(int,input().split()) # N: 이동 tn, BC_count: BC의 개수

    A_path = list(map(int,input().split()))
    B_path = list(map(int,input().split()))
    A_path.insert(0,0) # 시작할 때부터
    B_path.insert(0,0)

    # 시작점
    A = [1,1]
    B = [10,10]

    # 최대충전량 (음수가 될 수 없고)
    answer = 0

    # 받아서 저장도 해야됨
    # 리스트로 담아줄거임
    # 리스트의 크기를 미리 알 수 있음 -> 미리 세팅 plz

    # 각 충전기 정보
    BC_info = [0]*BC_count # BC_count 수만큼
    for i in range(BC_count):
        BC_count[i] = tuple(map(int,input().split())) # 변경되지 않을 정보는 튜플로 저장

    # 순차적으로 / 로직이 다임 ..?
    # 순차적으로 이동하며 충전하기
    for step in range(N+1): # T1, T2 말하는 거임

        # 1. A와  B를 이동하기 (이동 범위 밖을 검사할 필요 없다)
        a_dir, b_dir = A_path[step], B_path[step]
        A[0] += dr[a_dir]
        A[1] += dr[a_dir]
        B[0] += dr[b_dir]
        B[1] += dr[b_dir]

        # 2. A, B 각각이 충전 가능한 충전소를 파악하기
        #   > 충전 가능한 충전소의 인덱스를 저장하겠다
        A_BCs = []
        B_BCs = []
        for i in range(len(BC_info)): # BC_info 길이만큼
            BC_r ,BC_c, distance, charge = BC_info[i] # 4가지(2개는 좌표, 2개는 값)

            # a거리 이내이면 (abs 절대값)
            if abs(A[0] - BC_r) + abs(A[1] - BC_r) <= distance:
                A_BCs.append((i, charge))

            if abs(A[0] - BC_r) + abs(A[1] - BC_r) <= distance:
                B_BCs.append((i, charge))
        
        A_BCs.sort(key=lambda x:x[1], reverse=True)
        B_BCs.sort(key=lambda x:x[1], reverse=True)

        # 3. 최대 충전량이 확보 가능한 충전기를 고르기
        #    ㄱ. 충전기가 겹치지 않는 경우
        set_BCs = set(A_BCs).union(B_BCs)
        if len(set_BCs) == len(A_BCs) + len(B_BCs):

            # 0번 인덱스에는 충전량이 가장 높은 충전기 들어가있음 
            #걔의 충전량을 누적시켜줬다 그러면 B도 더해줘야됨
            if A_BCs:
                answer += A_BCs[0][1]
            if B_BCs:
                answer += B_BCs[0][1] 

        #    ㄴ. 충전기가 겹치는 경우 (분기를 잘 짜라 ?)
        else: # 여기서는 충전기 겹칠수밖에 없다
            anser += A_BCs[0][1]

            # A 최대 충전량의 번호랑 B의 최대 충전량의 번호가 같으면 
            # 양보하거나 양보 못하거나

            # 최고 충전기가 겹치는 경우
            if A_BCs[0][0] == B_BCs[0][0]:
                # A가 양보해야만 하는 경우
                if len(A_BCs) > 1 and len(B_BCs) == 1:
                    answer += A_BCs[1][1]
                # B가 양보해야만 하는 경우
                elif len(A_BCs) == 1 and len(B_BCs) > 1:
                    answer += B_BCs[1][1]
                # A와 B중 양보할 녀석을 비교해야 하는 경우
                elif len(A_BCs) > 1 and len(B_BCs) > 1:
                    answer += max(A_BCs[1][1], B_BCs[1][1])
            
            # 최고 충전기가 겹치지 않는 경우
            else:
                answer += B_BCs[0][1]
    print(f'#{tc} {answer}')
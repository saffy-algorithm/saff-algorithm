# 포탈
# 필요데이터
T = int(input()) #테스트 케이스 갯수
for tc in range(T):
    N = int(input()) # 방 갯수
    P = list(map(int, input().split())) # 방 번호 list

    # N=1 에서 기본으로 1 이동 (1->2)
    # 2번 부터 N-1 번까지는 방번호(room_num)-P+2 회 이동
    cnt = 0
    for room_num in range(N):
        if room_num+1 ==1:
            cnt += 1
        elif room_num+1 == N:
            cnt += 0
        else:
            cnt += (room_num+1)-P[room_num]+2
    print(f'#{tc+1} {cnt}')
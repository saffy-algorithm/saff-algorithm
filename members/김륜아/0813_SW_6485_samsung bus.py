# 삼성시의 버스 노선

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_num = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]
    
    cnt = [0] * P
    for p in range(P):
        for n in range(N):
            if bus_num[n][0] <= C[p] <= bus_num[n][1]:
                cnt[p] += 1
    
    print(f"#{tc}", *cnt)



# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input()) # 버스 노선의 수

#     # DAT 배열생성(인덱스를 1에서 5000)
#     dat = [0] * 5001

#     for _ in range(N):
#         A, B = map(int, input().split())
#         # A정류장 부터 B정류까지 counting
#         for i in range(A, B + 1):
#             dat[i] += 1

#     P = int(input()) # 정류장의 수
#     result = [] # 빈배열

#     for _ in range(P):
#         C = int(input())
#         result.append(dat[C])

#     print(f'#{tc}', end = ' ')
#     print(*result)



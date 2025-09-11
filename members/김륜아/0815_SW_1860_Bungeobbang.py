#   진기의 최고급 붕어빵

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    raw = (map(int, input().split()))
    print(raw)
    answer = "Possible"
    
    for i in range(N):
        made = (raw[i] // M) * K
        if made < i + 1:
            answer = "Impossible"
            break

    print(f"#{tc} {answer}")


# # 내 첫 풀이

# T = int(input())

# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())     # N명, M초, K개 붕어빵
#     raw = list(map(int, input().split()))   # 각 N명 초 단위
#     raw.sort()
    
#     # 붕어빵 M초에 K개 적립, 0번째는 빈 값
#     bung = [0] * (max(raw) + 1)

#     # 1초부터 max(raw)초번 반복
#     for t in range(M, max(raw)+1, M):
#         bung[t] += K

#     answer = 'Impossible'
    
#     # N명 반복
#     for i in range(N):
#         for bung_time in range(raw[i], 0, -1):
#             if bung[bung_time] >= 1:
#                 bung[bung_time] -= 1
#                 answer = 'Possible'
#                 break

#             else:
#                  answer = 'Impossible'
                 
            
#         if answer == 'Impossible':
#                 break
        
#     print(f"#{tc} {answer}")
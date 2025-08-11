# T = int(input())
# for tc in range(1, 1+T):
#     N= int(input())
#     numbers = list(map(int, input()))
#     count =0
#     count_lst = []
#     for i in range(N):
#         if numbers[i]==1:
#             count +=1
#             count_lst.append(count)
#         else:
#             count = 0
#     ans = max(count_lst)
#     print(ans)
#그리디(욕심쟁이) 알고리즘
# 완전탐색으로 풀면 모든 경우의 수를 탐색해야 하니 시간이 오래 걸린다.(시간초과)
# 최적의 선택을 한다.
# 나만의 전략대로 문제를 푼다.

# '1'이 등장하면 counting하면서 최대값 갱신

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    sequence = input()
    max_cnt = 0
    cnt =0
    # for문 순회 1. 인덱싱방식
    # 2. iterator 방식 순회
    for seq in sequence: # 파이써닉한 방식()
        if seq =='1':
            cnt+=1 #counting
            max_cnt = max(max_cnt, cnt) #최대값 갱신
        else:
            cnt =0 # count 초기화
    print(f'#{tc} {max_cnt}')
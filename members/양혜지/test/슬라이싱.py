# arr = list(map(int, input().split()))
# M = int(input())

# for i in range(len(arr) - M + 1):
#     sub = arr[i : i+M]
#     # 순 증가 수열인지 확인
#     switch = True
#     for j in range(M-1):
#         if sub[j] >= sub[j+1]:
#             switch = False
    
#     if switch == False:
#         print("no")
#     else:
#         print("yes")



def is_increase(arr):
    before = -101
    for i in range(1, len(arr)):
        if arr[i] > before:
            before = arr[i]
            continue
        else:
            return 0
        
    return 1

T = int(input())
for tc in range(1, T+1):

    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    answer = 0  # 순 증가 구간 개수

    # 올림
    K = N//M
    if N%M > 0:
        K +=1

    # 반복횟수 세팅에 대해 (K) 어려움을 겪는다 . .
    for count in range(K): 
        idx = count*M
        answer += is_increase(arr[idx:idx+M])

    print(f'#{tc} {answer}')


def is_increase(arr):
    before = -101  # 문제에서 입력 숫자가 -100 ~ 100 사이일 경우를 가정 (초기값으로 최소값보다 작게 설정)
    for i in range(1, len(arr)):
        if arr[i] > before:
            before = arr[i]
            continue
        else:
            return 0  # 하나라도 증가하지 않으면 0 반환

    return 1  # 모든 쌍이 증가하고 있으면 1 반환

T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = 0 

    # 배열을 M개씩 끊어서 순 증가 여부를 확인할 건데,
    # 전체 배열을 M씩 자를 수 있는 총 묶음 수(K)를 계산
    K = N // M  # M으로 나눈 몫만큼은 무조건 생김
    if N % M > 0:
        K += 1  # 나머지가 있으면 마지막에 남은 구간도 하나로 계산

    # 각 M 크기의 구간에 대해 반복
    for count in range(K): 
        idx = count * M  # 시작 인덱스
        # 배열을 idx부터 idx+M까지 슬라이싱하고, 그 구간이 순 증가이면 1 반환됨
        answer += is_increase(arr[idx:idx + M])

    # 결과 출력
    print(f'#{tc} {answer}')


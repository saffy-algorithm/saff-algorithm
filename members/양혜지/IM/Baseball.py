# 각 테케에 대해 N, K 선수의 수 N과 실력차이 K
# N개의 정수, 각 선수의 실력 합

# 출력
# 각 테케마다 최대로 구성할 수 있는 팀원의 수를 출력

# 문제 설명을 정리하면
# 주어진 선수들의 실력에서 특정 선수를 기준으로 실력 차이가 K 이하인 선수들을 모아
# 최대한 많은 팀원을 구성해야 함

# 모든 선수를 기준으로 최대한 가능한 팀원을 탐색하여 가장 큰 값을 출력

# 입력
# 3
# 4 2
# 6 4 2 3
# 4 3 
# 1 2 3 4
# 4 1
# 1 3 7 5

#1 (다소 간단)
# 조합
# 정렬
# IM은 비선형이 나오지 않음
# 이중 for문
# for 0 ~ (N-1) -> i를 인덱스로 지정했을 때
# 두번째 기준점은 i부터 진행되는 것이 맞음
# i ~ j 
# k 차이
# answer랑 계속 갱신
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    stats = list(map(int, input().split()))
    
    # 초기값 : 1명이면 팀을 짜는 걸 고려할 필요가 없음 따라서 1로 초기값 지정 
    # -> 2명이상 팀이 구성 되는지 안되는지만 체크하면 됨
    answer = 1
    stats.sort() # sorted(stats) 원본을 따로 저장하는건데 굳이 그럴필요없음 # 메모리효율
    # sort는 리턴을 아무것도 안줌 원본을 바꿀거니까 걍
    
    for i in range(N-2): # 끝놈은 필요없음 1명은 안되니까 그 앞
        temp = 1 # 팀원 누적할 임시변수
        # 초기값 1인 이유 j는 팀이 결성될때마다 하나씩 밀거임 그럼 팀원이 2명이상이라는거고 밀었을 때 더해서 2 이상이 나와야하니까 1로 설정
        for j in range(i+1, N): # i는 제외함 나는 제외해야하니까
            if stats[j] - stats[i] > K: # 앞사람에서 뒷사람 빼고
                break # 왜건다고 ?
                
            temp += 1 # 왜 else구분이 될수밖에없다고 ..?
        answer = max(answer, temp)
    print(f'#{tc} {answer}')

######################################################################

#2 (다소 어려움)
# 투포인터 / 슬라이딩 윈도우가 시간복잡도가 더 낮음
# 뒤는 고정시키고 앞에만 땡겨

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    stats = list(map(int, input().split()))
    
    answer = 1
    stats.sort()
    
    left = 0
    right = 0
    
    # 숫자가 불규칙적이라서 while
    # left가 밀릴 때는 안 될때, right가 밀릴 때는 될 때
    while right < N: # 아직 안 넘어 갔으면 계속 밀거다
        if stats[right] - stats[left] <= K:
            right +=1
            answer = max(answer, right - left)
            continue
        left += 1
    print(answer)
    
# 출력

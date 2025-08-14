# 스위치 켜고 끄기

# 대칭이 깨질 때까지
# 횟수 불규칙적 -> 여학생은 while
# 남자 명령은 배수를 걸었음
# 배수처리를 수월하게 하기 위해서 시작을 한 칸 미루어줌

###################################

# 필요 데이터

# N : 스위치의 수
# switches : 스위치의 상태 (입력받기)
# M : 명령의 수
# gender : 명령의 성별
# number : 명령의 번호
# idx :  남자 명령일 때 몇 배수인지 체크 용도
# l, r : 여자 명령을 수행하는 경우, 좌측 인덱스와 우측 인덱스


# 로직

# 1. N, switches, M 입력
# 2. M줄에 걸쳐서 명령을 입력받기(for 반복문)
#    ㄱ. 남자일 때
#        - number부터 배수에 대하여 상태를 스왑해주기 (명령수행)
#
#    ㄴ. 여자일 때
#        - number 변경
#        - 좌우 대칭 (l 지점과 r 지점의 값이 같을 때)를 만족할 때까지 반복
#           a. 해당 지점의 값을 스왑
#            b. l r 지점을 갱신

N = int(input())
switches = list(map(int,input().split()))
switches.insert(0, 0)

M = int(input())
for _ in range(M):
    gender, number = map(int, input().split())
    
    if gender == 1:
        # 배수가 길이를 너머섰을 때
        # 얼만큼 배수해줄지
        idx = 1
        while number*idx <= N:
            # 리스트 안쪽 -> 상태 스왑
            switches[number*idx] = (switches[number*idx]+1)%2
            idx += 1    
    
    # 여자쪽 연산 -> 값을 변경
    else:
        switches[number] = (switches[number]+1)%2
        l = number-1
        r = number+1
        
        # 스위치상으로 0 은 사용안함 / 현재 1부터 n까지 인덱스 사용중이기 때문
        # 따라서 1부터 조건
        while 1 <= l and r <= N and switches[l] == switches[r]:
            switches[l] = (switches[l]+1)%2
            switches[r] = (switches[r]+1)%2
            l -=1
            r +=1
            
# # 슬라이싱 (슬라이싱한 결과 복사 후 출력)
# i = 1
# while i <= N:
#     print(*switches[i:i*20])
#     i += 20

# 하나하나
for i in range(1, N+1):
    print(switches[i], end = ' ')
    if i % 20 == 0:
        print()
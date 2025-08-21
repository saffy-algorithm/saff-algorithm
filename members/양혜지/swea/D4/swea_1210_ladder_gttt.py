# 2에서 출발
# r=0 시 종료
# 상좌우만 봐
# 계속 올라가 내려가지마
# 옆에 0이 없으면 꺾어 ..?

T = 10
for tc in range(1, T+1):
    input()
    ladder = [list(map(int,input().split())) for _ in range (100)]
    
    for i in range(100):
        for j in range(100):
            
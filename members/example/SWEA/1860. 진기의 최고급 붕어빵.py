'''
- N명의 손님
- M초의 시간이 지나면 K개의 붕어빵을 만들 수 있다
'''
from collections import deque
 
 
def solution():
    N, M, K = map(int,input().split())
    arrived = list(map(int, input().split()))
    bongbread = []
    arrived.sort()
    arrived = deque(arrived)
     
    if arrived[0] == 0:
        return "Impossible"
     
    bongbread = 0
    for i in range(1, arrived[-1] + 1):
        if i % M == 0:
            bongbread += K
 
        while arrived and arrived[0] == i:
            if bongbread > 0:
                bongbread -= 1
                arrived.popleft()
            else:
                return "Impossible"
 
    return "Possible"
 
 
 
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')

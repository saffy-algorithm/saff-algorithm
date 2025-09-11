from collections import deque

T= int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    num_list = list(map(int,input().split()))

    cq = deque()


    for i in range(N):
            cq.append((i+1,num_list[0]))
            num_list.pop(0)
        

    count = N+1

    while len(cq)>1:
            number,cheeze = cq.popleft()
            half_cheeze = cheeze // 2

            if num_list:
                if half_cheeze == 0:
                        cq.append((count, num_list[0]))
                        num_list.pop(0)
                        count += 1
                else:
                    cq.append((number,half_cheeze))

            else:
                if half_cheeze != 0:
                    cq.append((number,half_cheeze))


    

    result = cq.pop()[0]

    print(f'#{tc} {result} ')


                
                


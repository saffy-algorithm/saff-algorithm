# from collections import deque
# T = 10
# for _ in range(10):
#     test_case = int(input())
#     nums = deque(map(int,input().split()))
#     cnt = 1
#     while 1:
#         num = nums.popleft() # 가장 왼쪽 숫자 pop
#         num-= cnt # cnt만큼 감소
#         cnt+=1 # cnt 1증가
#         if cnt==6: # cnt가 6이 됐다면 다시 1로 바꾸어 1사이클 종료
#             cnt = 1
#         if num<=0: # 0이하라면 0을 추가하고 반복문 종료
#             nums.append(0)
#             break
#         nums.append(num) # 그게 아니라면 감소한 num 다시 nums에 append
#     print(f'#{test_case}', end=" ")
#     for i in range(8):
#         print(f'{nums[i]}', end=' ')
#     print()



from collections import deque

for tc in range(10):
    tc_num = int(input())
    data = list(map(int, input().split()))
    data_deque = deque(data)  # 큐 생성
    cycle = 1

    while data_deque:
        num = data_deque.popleft() #가장 왼쪽 값을 반환, 오른쪽 끝은 pop()
        num -= cycle
        if num <= 0: #0보다 작아지거나 0일 경우 0으로 저장
            num = 0
            data_deque.append(num)
            break

        data_deque.append(num) #오른쪽 끝에 새로운 값을 추가, 왼쪽 끝은 appendleft()
        cycle += 1
        if cycle > 5:
            cycle = 1

    print(f"#{tc_num}", end=' ')
    for i in data_deque:
        print(f"{i}", end=' ')
    print()
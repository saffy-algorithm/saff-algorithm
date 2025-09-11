#   성공적인 공연 기획 (모든 사람들이 기립박수를 하기 위해 고용해야 하는 사람 수 세기)

T = int(input())

for tc in range (1, T+1):
    people = list(map(int, input()))
    
    people_sum = [0]*len(people)

    for i in range(1, len(people)):
        people_sum[0] = people[0]
        people_sum[i] = people[i] + people_sum[i-1]

    need = 0

    for num in range(1, len(people_sum)):
        if people_sum[num-1] < num:
            need += (num -people_sum[num-1])
            for sum_num in range(num, len(people_sum)):
                people_sum[sum_num] += (num -people_sum[num-1])
    
    print(f"#{tc} {need}")



# T = int(input())

# for tc in range(1, T+1):
#     people = list(map(int, input()))  # 각 자리 박수치는 사람 수
    
#     need = 0       # 고용해야 할 사람 수
#     standing = 0   # 현재까지 일어난 사람 수

#     for i in range(len(people)):
#         # i명 이상 서 있어야 하는데 부족하다면 고용
#         if standing < i:
#             need += (i - standing)
#             standing = i
#         # 현재 자리 관객도 더함
#         standing += people[i]
    
#     print(f"#{tc} {need}")
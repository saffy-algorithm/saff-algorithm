# T = int(input())

# for i in range(2, n-2):
#     lst = list(map(int,input().split()))
#     # 양 옆 2칸 중에 최대 높이

#     max_b = lst[i-2]
#     if  max_b [i-1] > # break


for test_case in range(1, 11):
 
    N = int(input())
    bud = list(map(int, input().split()))
 
    answer = []
    for i in range(2, N - 2):
        other_bud = bud[i - 2 : i] + bud[i + 1 : i + 3]
         
        if all(bud[i] > x for x in other_bud):
            answer.append(bud[i] - max(other_bud))
 
    print(f'#{test_case} {sum(answer)}')


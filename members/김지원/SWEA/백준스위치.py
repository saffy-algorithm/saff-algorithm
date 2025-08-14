switch_num = int(input())

switch = list(map(int,input().split()))

num =  int(input())

change = [list(map(int,input().split())) for _ in range(num)]

flag = False

for i in range(num):
    if change[i][0] == 1:
        for j in range(len(switch)):
            if (j+1) % change[i][1] == 0:
                switch[j] = 1- switch[j]

    else:
        m = change[i][1] - 1
        switch[m] = 1 - switch[m]
        for p in range(1,len(switch)):
            if 0<= m+p < len(switch) and 0<= m-p < len(switch):
                if switch[m+p] == switch[m-p]:
                    switch[m+p] = 1 - switch[m+p]
                    switch[m-p] = 1 - switch[m-p]

                else:
                    flag = True
                    break


count = 0
for num in switch:
    print(num, end = ' ')
    count += 1
    if count % 20 == 0:
        print()


#최두용 코드
'''
    1부터 시작
    학생에게 1~N개 자연수를 나눠줌
    성별과 받은 수에 따라 다름
    남학생: 스위치 번호가 받은 수의 배수이면 상태를 바꾼다
    여학생: 같은 번호 중심
        -   좌우가 대칭, 
        -   가장 많은 스위치를 포함하는 구간,
        -   모두 바꾸기
        -   갯수는 항상 홀수
    
'''
# 남은 1 여자는 2
# def convert_switch(s):
#     if s == 1:
#         return 0
#     else:
#         return 1

# N = int(input())
# switchs = list(map(int, input().split()))
# M = int(input())

# for _ in range(M):
#     sex, num = map(int, input().split())
#     idx = num - 1
#     if sex == 1:
#         for i in range(idx, N, num):
#             switchs[i] = convert_switch(switchs[i])

#     else:
#         switchs[idx] = convert_switch(switchs[idx])
#         i = 1
#         while (idx - i) >= 0 and (idx + i) < N:
#             if switchs[idx + i] != switchs[idx - i]:
#                 break
#             switchs[idx - i] = convert_switch(switchs[idx - i])
#             switchs[idx + i] = convert_switch(switchs[idx + i])
#             i += 1

# # print(switchs)
# for i in range(0, N, 20):
#     print(' '.join(map(str, switchs[i:i+20])))

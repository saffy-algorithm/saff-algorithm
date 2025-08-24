# 윤년
# 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
# 출력 : 윤년이면 1 아니면 0

# N = int(input())
# if (N%4 == 0 and N%100 != 0) or (N%400 ==0):
#      print('1')
# else:
#      print('0')

# 사분면 고르기
# 양수만 사분면 조건이니까 0은 미포함

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print('1')
# elif x > 0 and y < 0:
#     print('4')
# elif x < 0 and y > 0:
#     print('2')
# else:
#     print('3')

# 알람 시계
H, M = map(int, input().split())
if M < 45: # 분 단위가 45분보다 작을 때
    if H == 0: # 0시 이면
        H = 23
        M += 60
    else: # 0시가 아니면 (0시보다 크면))
        H -= 1
        M += 60

print(H, M-45)
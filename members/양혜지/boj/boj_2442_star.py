# 별 찍기 5

N = int(input())
# for i in range(1, N+1):
#     stars = '*' * (2*i-1)
#     empty = ' ' * (N-i)
#     print(empty + stars)

for i in range(1, N+1):
    print(' '*(N-i) + '*'*(2*i-1))
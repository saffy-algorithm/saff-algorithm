# 별 찍기 7

N = int(input())
for i in range(1, 2*N):
    star = '*'*(2*i-1)
    empty = ' '*(N-i)
    if i > N:
        for j in range(2*N, N, -1):
            star = '*'*(2*i-1)
            empty = ' '*(N-i)

print(empty + star)
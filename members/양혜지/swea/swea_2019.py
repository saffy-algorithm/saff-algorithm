N=int(input())
lst = []
for i in range(N+1): # 0부터 N까지 돌기 위해서, N+1을 end 값으로 지정
    lst.append(2**i) # i = 0부터 n까지 순회하기 위해서 (1씩 증가하는 순회) 선언
print(*lst) # 패킹 풀기 *
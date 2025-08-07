T = int(input())
answer = 0 # 먼저 정의(선언)해줘야 answer에 다 더해달라는 밑에 수식이 돌아감
for i in range(1, T+1):
    answer += i
 
print(answer)
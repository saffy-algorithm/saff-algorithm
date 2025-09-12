T = int(input())
day, month, threem, year = map(int, input().split())

# 1. 3달씩 묶어서 3달이랑 1달중에 머가 더 나은지 비교
# 2. -> 그 다음에 하루짜리랑 다시 비교
# 3. 다 하고 나서 다 더한거를 1년짜리랑 비교
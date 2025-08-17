N = int(input())
score = list(map(int, input().split()))

score.sort()

print(score[len(score)//2])
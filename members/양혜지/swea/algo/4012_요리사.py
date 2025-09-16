def comb(count, idx):
    global answer
    if count == N//2:
        A = picked
        B = [i for i in range(N) if i not in picked]
 
        A_score = 0
        B_score = 0
 
        for r in range(len(A)):
            for c in range(r + 1, len(A)):
                A_score += arr[A[r]][A[c]] + arr[A[c]][A[r]]
 
        for r in range(len(B)):
            for c in range(r + 1, len(B)):
                B_score += arr[B[r]][B[c]] + arr[B[c]][B[r]]
 
        answer = min(answer, abs(A_score-B_score))
        return
 
    for i in range(idx, N):
 
        ## 조합을 만들어서 A에게 주고, 나머지를 B에게 주기 때문에 결과적으로 조합이 중복이 됨
        if count == 0 and i != 0:
            continue  # 0번 재료를 고정해 중복 조합 차단 / 식재료를 고정해두고 하면 
        picked.append(food_number[i])
        comb(count + 1, i + 1)
        picked.pop()
 
 
T = int(input())
 
for tc in range(1, T+1):
 
    N = int(input()) 
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    food_number = [i for i in range(N)]
    answer = float('inf')
    picked = []
    comb(0,0)
 
    print(f'#{tc} {answer}')
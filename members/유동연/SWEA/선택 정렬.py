def selection(a,N):
    for i in range(N-1):
        min_idx=i # 첫 원소를 최소로 가정
        for j in range(i+1,N): # 자기 자신 다음거 부터 비교
            if a[min_idx] > a[j]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx], a[i]

a = [64, 25, 12, 22, 11]
N = len(a)
selection(a, N)

print("정렬 결과:", a)
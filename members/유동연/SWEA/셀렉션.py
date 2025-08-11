def selection(a, N): 
    for i in range(0, N): #n이 비교적 작을 때 유용
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[3]  # 마지막 원소 반환

# 데이터 준비
a = [64, 25, 12, 22, 11]
N = len(a)   # 리스트 길이

# 실행
last_value = selection(a, N)


print("마지막 원소:", last_value)

def binary(a, N, key):
    start = 0
    end = N-1
    while start<= end:
        middle = (start+end)//2
        if a[middle] == key:
            return middle
        elif a[middle]> key:
            end = middle - 1
        else:
            start = middle +1
    return -1
a = [1, 3, 5, 7, 9, 11, 13]
N = len(a)
key = 7
result = binary(a, N, key)
if result != -1:
    print(f"찾는 값 {key}는 인덱스 {result}에 있습니다.")
else:
    print(f"값 {key}를 찾을 수 없습니다.")
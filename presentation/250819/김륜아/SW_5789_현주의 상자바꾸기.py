#   현주의 상자 바꾸기 
#   (0으로 채워져있는 상자 번호가 밋밋해서 i숫자를 L번째 박스부터 R번째 박스까지 채우기)

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    raw = [0] * (N+1)

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for idx in range(L, R+1):
            raw[idx] = i
    print(f"#{tc}", *(raw[1:]))

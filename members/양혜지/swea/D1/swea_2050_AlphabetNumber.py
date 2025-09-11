alphabet = list(input())  # 입력 문자열을 리스트로 쪼갬
for i in alphabet:
    print(ord(i) - 64, end=" ")
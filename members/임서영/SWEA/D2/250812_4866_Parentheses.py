T = int(input())

match = {')':'(', '}':'{', ']':'['} #팝해서 쌍 맞는지 확인할 용도
answer = 1 #기본적으로 1

for tc in range(1, T+1):
    sen = input()
    check = []
    
    for word in sen:
        if word == '(' or word == '[' or word == '{':
            check.append(word)
        if word == ')' or word == ']' or word == '}':
            top = check.pop()
            if match[word] != top: #여는애랑 닫는애랑 쌍이 맞는지 검사
                answer = 0
                break
    if len(check) != 0:
        answer = 0

    print(f'#{tc} {answer}')
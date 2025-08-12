T = int(input())

match = {')':'(', '}':'{'} #팝해서 쌍 맞는지 확인할 용도
 
for tc in range(1, T+1):
    answer = 1 #기본적으로 1
    sen = input()
    check = []

    for word in sen:
        if word == '(' or word == '{':
            check.append(word)

        elif word == ')' or word == '}':
            if len(check) == 0: #조건1, 2
                answer = 0
                break

            if check[-1] == match[word]: #조건3
                check.pop()

            else:    
                answer = 0
                break

    if len(check) != 0: #조건1
        answer = 0

    print(f'#{tc} {answer}')
N = int(input())
str_list = list(input())

stack = []

for i in range(N):
    if str_list[i].isdigit() == True:
        stack.append(str_list[i])

    else:
        stack
        m = stack.pop()
        m = int(m) + int(str_list[i+1])
        stack.append(m)
        continue
    stack.append(str_list[i])

print(stack)
    
# 조합
numbers = [1,2,3,4,5]
M = 2
picked = []

def comb(cnt, idx):
    if cnt == M:
        print(picked)
        return
    
    for i in range(idx, len(numbers)):
        picked.append(numbers[i])
        comb(cnt+1, i+1)
comb(0, 0)

# 중복순열
# numbers = [1,2,3,4,5]
# M = 2
# picked = []
# def perm_dupli(cnt):
#     if cnt == M:
#         print(picked)
#         return

#     for i in range(len(numbers)):
#         picked.append(numbers[i])
#         perm_dupli(cnt+1)
#         picked.pop()
# perm_dupli(0)

# 순열
# numbers = [1,2,3,4,5]
# M = 2
# picked = []
# visited = [0] * len(numbers)
# def perm_dupli(cnt):
#     if cnt == M:
#         print(picked)
#         return

#     for i in range(len(numbers)):
#         if not visited[i]:
#             picked.append(numbers[i])
#             visited[i] = 1
#             perm_dupli(cnt+1)
#             picked.pop()
#             visited[i] = 0
# perm_dupli(0)

# 중복조합
# numbers = [1,2,3,4,5]
# M = 2
# picked = []

# def comb_dup(cnt, idx):
#     if cnt == M:
#         return
    
#     for i in range(idx, len(numbers)):
#         picked.append(numbers[i])
#         comb_dup(cnt+1, i)
#         picked.pop()
# comb_dup(0, 0)
T = int(input())
 
for t in range(T):
    tc, N = input().split()
    pnum_lst = list(input().split())
 
    pnum = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
 
    new_list = []
 
    for i in pnum:
        for num in pnum_lst:
            if i == num:
                new_list.append(num)
    result = ' '.join(new_list)
 
    print(f'{tc} {result}')
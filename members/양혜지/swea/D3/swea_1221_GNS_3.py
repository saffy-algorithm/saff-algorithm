T = int(input())
for tc in range(1, T + 1):
    st, N = input().split()
    N = int(N)
 
    nums = {
                "ZRO": 0
               , "ONE": 1
               , "TWO": 2
               , "THR": 3
               , "FOR": 4
               , "FIV": 5
               , "SIX": 6
               , "SVN": 7
               , "EGT": 8
                , "NIN": 9
    }
 
    sort_list = [0] * N
    inner_list = []
    words = list(input().split())
    k_words = [*nums]
 
    for i in range(10):
        times = words.count(k_words[i])
        inner_list.append((k_words[i] + ' ') * times)
 
    answer = ''.join(inner_list)
    print(st)
    print(answer.strip())
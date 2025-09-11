#   쇠막대기 자르기

T = int(input())

for tc in range(1, T+1):
    raw = input()
    
    # 쇠막대기 개수
    metal = 0

    # '(' 카운트 -> 레이저 만나면 '(' 개수만큼 쇠막대기 생김
    cnt_start = 0

    for idx in range(len(raw)):
        if raw[idx] == '(' and raw[idx+1] != ')':
            cnt_start += 1
        elif raw[idx] == '(' and raw[idx+1] == ')':
            metal += cnt_start

        # ')' 만나면 '(' 카운트 -1, metal 카운트 +1
        elif raw[idx] == ')' and raw[idx-1] != '(':
            cnt_start -= 1
            metal += 1

    print(f"#{tc} {metal}")
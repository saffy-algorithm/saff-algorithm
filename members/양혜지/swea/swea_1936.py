a, b = map(int,  input().split())
 
# 아래의 조건 중 하나라도 해당되면 B를 출력한다
# A가 1(가위)이고 B가 2(바위)인 경우
# A가 2(바위)이고 B가 3(보)인 경우
# A가 3(보)이고 B가 1(가위)인 경우
# 위 조건 중 만족하는 조건이 하나라도 없다면 A를 출력한다
 
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print('B')
else:
    print('A')
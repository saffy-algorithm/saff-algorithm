switch_num = int(input())

switch = list(map(int,input().split()))

num =  int(input())

change = [list(map(int,input().split())) for _ in range(num)]

flag = False

for i in range(num):
    if change[i][0] == 1:
        for j in range(len(switch)):
            if (j+1) % change[i][1] == 0:
                switch[j] = 1- switch[j]

    else:
        m = change[i][1] - 1
        switch[m] = 1 - switch[m]
        for p in range(1,len(switch)):
            if 0<= m+p < len(switch) and 0<= m-p < len(switch):
                if switch[m+p] == switch[m-p]:
                    switch[m+p] = 1 - switch[m+p]
                    switch[m-p] = 1 - switch[m-p]

                else:
                    flag = True
                    break


count = 0
for num in switch:
    print(num, end = ' ')
    count += 1
    if count % 20 == 0:
        print()



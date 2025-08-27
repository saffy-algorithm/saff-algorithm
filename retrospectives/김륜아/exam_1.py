T = int(input())
for tc in range(1, T+1):
    N = int(input())

    nums = list(map(int, input().split()))
    print(nums)

    cnt = 0
    i = 0       #current position

    while i < N - 1:
        if nums[i] == 0:
            i += 1
            cnt += 1
        elif nums[i] != 0:
            s = nums[i]     # s: temporarily save nums[i]
            nums[i] = 0
            i = s - 1
            cnt += 1

    print(cnt)
        


    
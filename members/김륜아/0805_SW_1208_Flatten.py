
for tc in range(1, 11):
	dump_num = int(input())
	dump_list = list(map(int, input().split()))

	for _ in range(dump_num):

		idx_max_num = dump_list.index(max(dump_list))
		dump_list[idx_max_num] -= 1

		idx_min_num = dump_list.index(min(dump_list))
		dump_list[idx_min_num] += 1

	answer = max(dump_list) - min(dump_list)

	print(f"#{tc} {answer}")

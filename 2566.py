# https://www.acmicpc.net/problem/2566

import sys
mtx = []
for i in range(9):
    mtx.append(list(map(int, sys.stdin.readline().split())))

maxnum_list = []
maxidx_list = []

for row in mtx:
    maxnum_list.append(max(row))
    maxidx_list.append(row.index(max(row)))

max_result = max(maxnum_list)
idx = maxnum_list.index(max_result)
print(max_result)
print(idx + 1, maxidx_list[idx] + 1)

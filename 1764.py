# https://www.acmicpc.net/problem/1764
import sys

n, m = map(int, sys.stdin.readline().strip().split())

listen = [sys.stdin.readline().strip() for i in range(n)]
see = [sys.stdin.readline().strip() for i in range(m)]

ls_dict = {}

for l in listen:
    if l in ls_dict:
        ls_dict[l] += 1
    else:
        ls_dict[l] = 1

for s in see:
    if s in ls_dict:
        ls_dict[s] += 1
    else:
        ls_dict[s] = 1

sorted_dict = sorted(ls_dict.items())

ls_list = []
cnt = 0

for key, value in sorted_dict:
    if value == 2:
        ls_list.append(key)
        cnt += 1

print(cnt)
for i in ls_list:
    print(i, end=' ')

# https://www.acmicpc.net/problem/25192
import sys

n = int(sys.stdin.readline().strip())

member = {}
cnt = 0
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    if tmp == "ENTER":
        for key, value in member.items():
            if value == 1:
                cnt += 1
        member = {}
    else:
        if tmp not in member:
            member[tmp] = 1

for key, value in member.items():
    if value == 1:
        cnt += 1
print(cnt)

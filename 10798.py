# https://www.acmicpc.net/problem/10798
import sys

data = []
cnt = 0
for i in range(5):
    datum = list(sys.stdin.readline().strip())
    data.append(datum)
    cnt += len(datum)

tmp = ''
while len(data) != 0:
    if len(tmp) == cnt:
        break
    for s in data:
        if len(s) != 0:
            tmp += s.pop(0)
print(tmp)

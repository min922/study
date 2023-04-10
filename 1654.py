# https://www.acmicpc.net/problem/1654
import sys

k, n = map(int, sys.stdin.readline().split())
data = []
for _ in range(k):
    data.append(int(sys.stdin.readline().strip()))
start = 1
end = max(data)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for elt in data:
        cnt += (elt // mid)
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)

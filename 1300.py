# https://www.acmicpc.net/problem/1300
import sys

a = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

start, end = 1, k
ans = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in range(1, a + 1):
        tmp += min(mid // i, a)  # B[mid]보다 작은 수들 갯수 세가
    if tmp >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)

# https://www.acmicpc.net/problem/3273
import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().strip())
data.sort()

cnt = 0
left, right = 0, n - 1

while left < right:
    tmp = data[left] + data[right]
    if tmp == x:
        cnt += 1
        left += 1  # 다음 탐색
    elif tmp < x:
        left += 1  # x보다 작으면 왼쪽++
    else:
        right -= 1  # x보다 크면 오른쪽--
print(cnt)

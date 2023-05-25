# https://www.acmicpc.net/problem/1806
import sys

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
tmp = 0
min_len = n + 1
while True:
    if tmp >= s:
        min_len = min(min_len, right - left)  # 최소길이 저장
        tmp -= data[left]  # 더 짧은게 있을수도 있으니
        left += 1  # 다음 탐색 위해 left++
    elif right == n:
        break
    else:
        tmp += data[right]
        right += 1

if min_len == n + 1:
    print(0)
else:
    print(min_len)

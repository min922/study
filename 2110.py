# https://www.acmicpc.net/problem/2110
import sys

n, c = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline().strip()) for _ in range(n)]
house.sort()

start, end = 1, house[-1] - house[0]  # 집 사이의 최소, 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    now = house[0]

    for i in range(1, n):
        if house[i] >= now + mid:
            cnt += 1
            now = house[i]

    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)

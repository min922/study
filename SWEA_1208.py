# SWEA 1208. [S/W 문제해결 기본] 1일차 - Flatten
import sys

for i in range(10):
    n = int(sys.stdin.readline().strip())
    data = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    while True:
        max_index = data.index(max(data))
        min_index = data.index(min(data))
        if cnt == n:
            print("#{} {}".format(i + 1, data[max_index] - data[min_index]))
            break
        else:
            data[max_index] -= 1
            data[min_index] += 1
            cnt += 1

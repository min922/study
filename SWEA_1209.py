# SWEA 1209. [S/W 문제해결 기본] 2일차 - Sum 
import sys

for _ in range(10):
    T = int(sys.stdin.readline().strip())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(100)]
    result = []
    for row in data:
        result.append(sum(row))
    for i in range(100):
        tmp = [elt[i] for elt in data]
        result.append(sum(tmp))
    cnt = 0
    right = []
    for i in range(100):
        right.append(data[i][cnt])
        cnt += 1
    result.append(sum(right))
    left = []
    cnt = 99
    for i in range(100):
        left.append(data[i][cnt])
        cnt -= 1
    result.append(sum(left))
    print("#{} {}".format(T, max(result)))

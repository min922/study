# SWEA 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
import sys
from collections import deque

for _ in range(10):
    t = int(sys.stdin.readline().strip())
    num = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 1
    while True:
        tmp = num.popleft() - cnt
        if tmp <= 0:
            tmp = 0
        num.append(tmp)
        cnt += 1
        if cnt == 6:
            cnt = 1
        if tmp == 0:
            break
    print("#" + str(t), end=' ')
    for n in num:
        print(n, end=' ')

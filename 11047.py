# https://www.acmicpc.net/problem/11047 
import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().strip()))
coin.reverse()

cnt = 0
for i in coin:
    cnt += k // i  # 동전갯수
    k -= (k // i) * i  # k=4200, i=1000일 경우:4200 -= 4*1000
    if k == 0:
        print(cnt)
        break

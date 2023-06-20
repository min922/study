# https://www.acmicpc.net/problem/24313
import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().strip())
n0 = int(sys.stdin.readline().strip())

check = 1
for n in range(n0, 101):
    fn = a1 * n + a0
    if fn > c * n:  # f가 O(n) 만족 못할때
        check = 0
        break
print(check)

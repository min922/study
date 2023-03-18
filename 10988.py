# https://www.acmicpc.net/problem/10988
import sys

pel = sys.stdin.readline().strip()

if pel == pel[::-1]:
    print(1)
else:
    print(0)

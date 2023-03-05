# https://www.acmicpc.net/problem/10807
import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline().strip())
print(data.count(v))

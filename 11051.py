# https://www.acmicpc.net/problem/11051
import sys, math

n, r = map(int, sys.stdin.readline().split())
result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
print(result % 10007)

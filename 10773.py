# https://www.acmicpc.net/problem/10773
import sys

k = int(sys.stdin.readline().strip())
stack = []
for i in range(k):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))

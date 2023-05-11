# https://www.acmicpc.net/problem/9063
import sys

n = int(sys.stdin.readline().strip())
x_axis = []
y_axis = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x_axis.append(a)
    y_axis.append(b)

x = max(x_axis) - min(x_axis)
y = max(y_axis) - min(y_axis)

print(x * y)

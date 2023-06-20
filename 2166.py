# https://www.acmicpc.net/problem/2166
import sys

n = int(sys.stdin.readline().strip())

x_axis, y_axis = [], []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x_axis.append(a)
    y_axis.append(b)
x_axis.append(x_axis[0])
y_axis.append(y_axis[0])
# 신발끈공식 사용

dx, dy = 0, 0
for i in range(n):
    dx += x_axis[i] * y_axis[i + 1]
    dy += y_axis[i] * x_axis[i + 1]
area = abs((dx - dy) / 2)
print(round(area, 1))

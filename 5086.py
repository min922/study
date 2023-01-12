# https://www.acmicpc.net/problem/5086

def find(a, b):
    if a < b:
        if (b // a) == (b / a):
            return "factor"
    elif a > b:
        if (a // b) == (a / b):
            return "multiple"
    return "neither"

import sys
data = []
a, b = -1, -1
while a != 0 and b != 0:
    a, b = map(int, sys.stdin.readline().split())
    data.append([a, b])
for i in range(len(data) - 1):
    print(find(data[i][0], data[i][1]))

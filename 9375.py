# https://www.acmicpc.net/problem/9375
import sys

T = int(sys.stdin.readline().strip())

for t in range(T):
    n = int(sys.stdin.readline().strip())
    cloth = {}
    for i in range(n):
        name, kind = sys.stdin.readline().split()
        if kind in cloth:
            cloth[kind].append(name)
        else:
            cloth[kind] = [name]
    result = 1
    for key, item in cloth.items():
        result *= (len(cloth[key]) + 1)
    print(result - 1)

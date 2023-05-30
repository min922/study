# https://www.acmicpc.net/problem/1541
import sys

eq = sys.stdin.readline().strip().split('-')
num = []
for elt in eq:
    if '+' in elt:
        tmp = list(map(int, elt.split('+')))
        num.append(sum(tmp))
    else:
        num.append(int(elt))

result = num[0] - sum(num[1:])
print(result)

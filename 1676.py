# https://www.acmicpc.net/problem/1676
import math
import sys

N = int(sys.stdin.readline().strip())

fac = str(math.factorial(N))[::-1]

result = 0
for f in fac:
    if int(f) == 0:
        result += 1
    else:
        break
print(result)

# https://www.acmicpc.net/problem/11005
import sys

n, b = map(int, sys.stdin.readline().split())

tmp = []
while n != 0:
    tmp.append(n % b)
    n = n // b

result = ""
for i in tmp:
    if i < 10:
        result += str(i)
    else:
        result += chr(i + 55)
print(result[::-1])

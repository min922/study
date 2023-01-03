# https://www.acmicpc.net/problem/11478
import sys

given = sys.stdin.readline().strip()

result = set()

for idx in range(1, len(given) + 1):
    start = 0
    while start + idx <= len(given):
        result.add(given[start:start+idx])
        start += 1
print(len(result))

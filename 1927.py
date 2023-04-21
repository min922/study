# https://www.acmicpc.net/problem/1927
import heapq
import sys

n = int(sys.stdin.readline().strip())
heap = []

for _ in range(n):
    data = int(sys.stdin.readline().strip())
    if data == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, data)

# https://www.acmicpc.net/problem/11286
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
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(data), data))  # 튜플을 넣으면 첫 번째 요소로 최소힙이 구현됨

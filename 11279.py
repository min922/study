# https://www.acmicpc.net/problem/11279
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
            print(-heapq.heappop(heap))  # push할때 -를 붙혔으므로 pop할때 제거해줌
    else:
        heapq.heappush(heap, -data)  # heapq는 최소힙이므로 최대힙을 구현하려면 음수로 해야함

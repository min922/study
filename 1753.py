# https://www.acmicpc.net/problem/1753
import sys
import heapq

INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, [0, start])  # [거리, 시작노드]
    distance[start] = 0  # 시작점 자신은 0
    while queue:
        dist, now = heapq.heappop(queue)  # 거리와 현재 위치
        if distance[now] >= dist:  # 현재 거리가 최단거리이면
            for i in graph[now]:  # 현재 위치에 연결된 노드 탐색
                cost = dist + i[1]  # 연결된 노드로 가는 거리
                if cost < distance[i[0]]:  # 가는 비용이 최소이면
                    distance[i[0]] = cost  # 최소인 곳으로 가기
                    heapq.heappush(queue, [cost, i[0]])  # 다음 노드 push


v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline().strip())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

dijkstra(k)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

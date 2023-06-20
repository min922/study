# https://www.acmicpc.net/problem/11779
import sys
import heapq

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
path = [0 for _ in range(n + 1)]  # 이전 노드 저장
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
start, end = map(int, sys.stdin.readline().split())
INF = 10e9


def dijkstra(start):
    queue = []
    distance = [INF for _ in range(n + 1)]
    heapq.heappush(queue, [start, 0])
    distance[start] = 0
    while queue:
        now, dist = heapq.heappop(queue)
        if dist <= distance[now]:  # 최소 거리일때만 탐색(이 조건 없으면 시간초과남)
            for node, d in graph[now]:  # 현재 위치에 연결된 노드에 대해
                next_dist = dist + d  # 연결된 노드로 가는 거리
                if distance[node] > next_dist:  # 최단거리이면
                    distance[node] = next_dist  # 거리 저장
                    path[node] = now  # 이전 노드 저장
                    heapq.heappush(queue, [node, next_dist])  # 다음 탐색
    return distance


cost = dijkstra(start)
print(cost[end])
result = []
tmp = end
while tmp != start:  # 마지막 노드부터 시작해서
    result.append(tmp)  # 이전노드를 추가하고
    tmp = path[tmp]  # 노드 갱신
result.append(start)
print(len(result))
print(*reversed(result))

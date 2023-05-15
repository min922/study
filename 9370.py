# https://www.acmicpc.net/problem/9370
import sys
import heapq


def dijkstra(start):
    queue = []
    distance = [INF for _ in range(n + 1)]
    heapq.heappush(queue, [start, 0])
    distance[start] = 0
    while queue:
        now, dist = heapq.heappop(queue)
        for node, d in graph[now]:  # 현재 위치에 연결된 노드에 대해
            next_dist = dist + d  # 연결된 노드로 가는 거리
            if distance[node] > next_dist:  # 최단거리이면
                distance[node] = next_dist  # 거리 저장
                heapq.heappush(queue, [node, next_dist])  # 다음 탐색
    return distance


INF = 10e9
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    cand = [int(sys.stdin.readline().strip()) for _ in range(t)]
    start = dijkstra(s)  # 출발점에서 시작하는 다익스트라
    g_start = dijkstra(g)  # g에서 시작
    h_start = dijkstra(h)  # h에서 시작
    result = []
    for i in cand:  # 시작->g->h->후보지 / 시작->h->g->후보지 거리 = 시작->후보지 거리랑 같으면 추가(최단거리)
        if start[g] + g_start[h] + h_start[i] == start[i] or start[h] + h_start[g] + g_start[i] == start[i]:
            result.append(i)
    result.sort()
    print(*result)

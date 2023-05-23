# https://www.acmicpc.net/problem/11657
import sys


# 다익스트라는 음수간선순환이 있을경우 사용불가
def bellmanford(start):
    distance[start] = 0
    for i in range(1, n + 1):
        for j in range(m):
            now, next, cost = graph[j]
            # n번 라운드 통해 모든 간선을 최단 거리로 갱신
            if distance[now] != INF and distance[next] > distance[now] + cost:
                # 최단거리일 경우
                distance[next] = distance[now] + cost
                if i == n:  # n번째에서도 값이 바뀐다면 음수 순환 존재 -> return
                    return True
    return False


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
INF = 10e9
distance = [INF for _ in range(n + 1)]

is_cycle = bellmanford(1)
if is_cycle: # 음수순환 싸이클이 있으면
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])

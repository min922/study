# https://www.acmicpc.net/problem/14889

import sys


def startlink(depth, idx):
    global min_diff
    if depth == N // 2: # 사람 중 반이 한팀이 되었을 때
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: # visited가 True면 start팀
                    start += table[i][j] # start팀 점수 합계
                elif not visited[i] and not visited[j]: # visited가 False면 link팀
                    link += table[i][j] # link팀 점수 합계
        min_diff = min(min_diff, abs(start - link))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            startlink(depth + 1, i + 1)
            visited[i] = False


N = int(sys.stdin.readline().strip())

visited = [False for _ in range(N)]

table = []
for i in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))

min_diff = int(1e9)
startlink(0, 0)

print(min_diff)

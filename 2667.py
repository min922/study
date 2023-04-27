# https://www.acmicpc.net/problem/2667
import sys
from collections import deque


def bfs(r, c):
    dx = [0, 0, 1, -1]  # 이동 좌표
    dy = [1, -1, 0, 0]
    home[r][c] = 0  # 맨 처음 시작 집 방문
    queue = deque([[r, c]])
    cnt = 1  # 각 단지내 집의 수를 세는 변수
    while queue:  # queue가 빌때까지
        x, y = queue.popleft()
        home[x][y] = 0
        for i in range(4):
            nx = x + dx[i]  # 왼, 오 이동
            ny = y + dy[i]  # 상, 하 이동

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue  # 범위 벗어났을 경우
            if home[nx][ny] == 1:  # 방문 안한곳
                home[nx][ny] = 0  # 방문 표시
                queue.append([nx, ny])
                cnt += 1
    return cnt


n = int(sys.stdin.readline().strip())
home = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if home[i][j] == 1:  # 집이 있는 곳이면 bfs로 탐색
            count = bfs(i, j)
            result.append(count)
result.sort()

print(len(result))  # 총 단지 수
for _ in result:
    print(_)

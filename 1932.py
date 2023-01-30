# https://www.acmicpc.net/problem/1932
import sys

n = int(sys.stdin.readline().strip())

tri = []
for i in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0:  # 맨 앞이면 맨 앞만 더함
            tri[i][j] += tri[i - 1][j]
        elif j == i:  # 맨 뒤면 맨 뒤만 더함
            tri[i][j] += tri[i - 1][j - 1]
        else:  # 위의 오른쪽, 왼쪽 비교해서 큰것 더해줌
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

print(max(tri[-1]))
# 맨 마지막 행의 최대값 출력

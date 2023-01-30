# https://www.acmicpc.net/problem/1149
import sys

N = int(sys.stdin.readline().strip())

house = []

for i in range(N):
    house.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    house[i][0] = min(house[i - 1][1], house[i - 1][2]) + house[i][0]
    house[i][1] = min(house[i - 1][0], house[i - 1][2]) + house[i][1]
    house[i][2] = min(house[i - 1][0], house[i - 1][1]) + house[i][2]
# 합의 최솟값을 구해야하므로 각 줄의 최소값만을 더하는 것이 답이 아님
# house[1][0], house[1][1], house[1][2]를 초깃값으로 하여 최소값을 구해나감

print(min(house[-1][0], house[-1][1], house[-1][2]))
# 맨 마지막에 최종 값이 저장되어 있으므로 그 중 최소값 출력

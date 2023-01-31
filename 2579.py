# https://www.acmicpc.net/problem/2579
import sys

n = int(sys.stdin.readline().strip())

stair = []
for i in range(n):
    stair.append(int(sys.stdin.readline().strip()))

dp = []
if n == 1:
    dp.append(stair[0])  # 맨 첫 계단
elif n == 2:
    dp.append(stair[0])  # 맨 첫 계단
    dp.append(max(stair[1], stair[0] + stair[1]))  # 두 번째 가는 방법 2 혹은 1-1
elif n == 3:
    dp.append(stair[0])  # 맨 첫 계단
    dp.append(max(stair[1], stair[0] + stair[1]))  # 두 번째 가는 방법 2 혹은 1-1
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))  # 세번째 가는 방법 1-2 혹은 2-1
else:
    dp.append(stair[0])  # 맨 첫 계단
    dp.append(max(stair[1], stair[0] + stair[1]))  # 두 번째 가는 방법 2 혹은 1-1
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))  # 세번째 가는 방법 1-2 혹은 2-1

    for i in range(3, n):
        dp.append(max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i]))
    # 연속 세 계단 오르면 안되니까 현재 위치의 세번째 전부터 카운트
    # 1-1-1은 불가능하니 1-2 혹은 2-1로 올라가서 현재 위치에 도달해야함

print(dp[-1])

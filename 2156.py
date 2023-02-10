# https://www.acmicpc.net/problem/2156
import sys

n = int(sys.stdin.readline().strip())

data = []
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))

dp = []

if n == 1:
    dp.append(data[0])
elif n == 2:
    dp.append(data[0])
    dp.append(max(data[0], data[1], data[0] + data[1]))
elif n == 3:
    dp.append(data[0])
    dp.append(max(data[0], data[1], data[0] + data[1]))
    dp.append(max(data[0] + data[1], data[0] + data[2], data[1] + data[2]))
else:
    dp.append(data[0]) 
    dp.append(max(data[0], data[1], data[0] + data[1]))
    dp.append(max(data[0] + data[1], data[0] + data[2], data[1] + data[2]))
    for i in range(3, n):
        dp.append(max(dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i], dp[i - 1])) # xoxo / oxoo / xxox 

print(max(dp))

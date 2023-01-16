# https://www.acmicpc.net/problem/2587
import sys

data = []
for i in range(5):
    data.append(int(sys.stdin.readline().strip()))
data.sort()
print(sum(data) / 5) # 평균
print(data[2]) # 중간값

# https://www.acmicpc.net/problem/1931
import sys

n = int(sys.stdin.readline().strip())
time = []
for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))
time.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간이 빠른 순으로 정렬 후 끝나는 시간이 같으면 시작하는 시간이 빠른 순으로 정렬
cnt = [time[0]]
for i in range(1, n):
    if time[i][0] >= cnt[-1][1]: # 시작하는 시간이 전의 끝나는 시간과 같거나 클 때 회의 가능
        cnt.append(time[i])
print(len(cnt))

# https://www.acmicpc.net/problem/2738
import sys

mtx1 = []
mtx2 = []

n, m = map(int,sys.stdin.readline().split()) # row, column

for i in range(n):
    mtx1.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    mtx2.append(list(map(int, sys.stdin.readline().split())))

result = []
for item1, item2 in zip(mtx1, mtx2):
    tmp = []
    for k in range(m):
        tmp.append(item1[k] + item2[k])
    result.append(tmp)

for i in result:
    for j in i:
        print(j, end=' ')
    print("")

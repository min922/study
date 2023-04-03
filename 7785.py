# https://www.acmicpc.net/problem/7785
import sys

n = int(sys.stdin.readline().strip())

people = {}
for _ in range(n):
    tmp = sys.stdin.readline().split()
    if tmp[1] == 'enter':
        people[tmp[0]] = True
    elif tmp[1] == 'leave':
        people.pop(tmp[0])

people = sorted(people, reverse=True)

for i in people:
    print(i)

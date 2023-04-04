# https://www.acmicpc.net/problem/1920
import sys

n = int(sys.stdin.readline().strip())
given = list(map(int, sys.stdin.readline().split()))
given.sort()
m = int(sys.stdin.readline().strip())
find = list(map(int, sys.stdin.readline().split()))

for i in find:
    start = 0
    end = n - 1
    not_exist = True

    while start <= end:
        mid = (start + end) // 2
        if i == given[mid]:
            not_exist = False
            print(1)
            break
        elif i > given[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if not_exist:
        print(0)

# https://www.acmicpc.net/problem/2164
import sys

n = int(sys.stdin.readline().strip())

queue = list(range(1, n + 1))

while len(queue) > 1:
    if len(queue) % 2:
        tmp = [queue[-1]]
        tmp.extend(queue[1::2])
        queue = tmp
    else:  # 버리고 아래로 옮기는 과정에서 홀수번째항들은 어차피 다 없어짐
        queue = queue[1::2]
print(queue[0])

# n = 1 -> 1
# n = 2 -> 2
# n = 3 -> 123 / 32 / 2
# n = 4 -> 1234 / 342 / 24 / 4
# n = 5 -> 12345 / 3452 / 524 / 42 / 2
# n = 6 -> 123456 / 34562 / 5624 / 246 / 64 / 4
# n = 7 -> 1234567 / 345672 / 56724 / 7246 / 462 / 26 / 6

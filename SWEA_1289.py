# SWEA 1289. 원재의 메모리 복구하기
import sys

t = int(sys.stdin.readline().strip())
for T in range(t):
    data = list(map(int, list(sys.stdin.readline().strip())))
    result = 0
    for i in range(len(data) - 1):
        if i == 0 and data[i] == 1:
            result += 1
        if data[i] != data[i + 1]:
            result += 1
    print("#{} {}".format(T + 1, result))

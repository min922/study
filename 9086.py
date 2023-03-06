# https://www.acmicpc.net/problem/9086
import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    string = sys.stdin.readline().strip()
    print("{}{}".format(string[0], string[-1]))

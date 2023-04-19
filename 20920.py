# https://www.acmicpc.net/problem/20920
import sys

n, m = map(int, sys.stdin.readline().split())
word_dict = {}

for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

result = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in result:
    print(i[0])

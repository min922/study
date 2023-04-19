# https://www.acmicpc.net/problem/2630
import sys

n = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white, blue = 0, 0


def sol(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                sol(x, y, n // 2)
                sol(x, y + n // 2, n // 2)
                sol(x + n // 2, y, n // 2)
                sol(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


sol(0, 0, n)
print(white)
print(blue)

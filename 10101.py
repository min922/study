# https://www.acmicpc.net/problem/10101
import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

if a + b + c != 180:
    print("Error")
elif a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif a == b or b == c or c == a:
    print("Isosceles")
else:
    print("Scalene")

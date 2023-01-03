# https://www.acmicpc.net/problem/1269
import sys

n, m = map(int, sys.stdin.readline().strip().split())

A = set(map(int,sys.stdin.readline().split()))
B = set(map(int,sys.stdin.readline().split()))

print(len(A-B) + len(B-A))

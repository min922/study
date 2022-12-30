# https://www.acmicpc.net/problem/10815
import sys

def sol(elt, card_list, start, end):
    while start <= end:
        mid = (start + end) // 2
        if card_list[mid] == elt:
            return 1
        elif card_list[mid] < elt:
            start = mid + 1
        elif card_list[mid] > elt:
            end = mid - 1
    return 0

n = int(sys.stdin.readline())
mine = list(map(int, sys.stdin.readline().strip().split())) # 내카드
m = int(sys.stdin.readline())
given = list(map(int, sys.stdin.readline().strip().split())) # 구분해야함

sort_mine = list(sorted(mine))

for elt in given:
    print(sol(elt, sort_mine, 0, n-1), end=" ")


# 시간초과
# for elt in given:
#     if elt in mine:
#         print(1, end=" ")
#     else:
#         print(0, end=" ")
# 전부 탐색해서 시간이 오래걸림 -> 이진탐색 알고리즘 사용함

# https://www.acmicpc.net/problem/10816
import sys

n = int(sys.stdin.readline())
mine = list(map(int, sys.stdin.readline().strip().split())) # 내카드
m = int(sys.stdin.readline())
given = list(map(int, sys.stdin.readline().strip().split())) # 구분해야함

card_dict = {}

for elt in mine:
    if elt in card_dict:
        card_dict[elt] += 1
    else:
        card_dict[elt] = 1

for card in given:
    if card in card_dict:
        print(card_dict[card], end=" ")
    else:
        print(0, end=" ")

# list.count()의 시간 복잡도 = O(n)

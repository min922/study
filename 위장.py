# 프로그래머스 위장
def solution(clothes):
    dict = {}
    for i in clothes:
        kind, name = i[1], i[0]
        if kind not in dict:
            dict[kind] = 1
        else:
            dict[kind] += 1
    result = 1
    for key, value in dict.items():
        result *= (value + 1)
    return result - 1

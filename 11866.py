# https://www.acmicpc.net/problem/11866
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
circle = deque(list(range(1, n + 1)))

result = "<"
cnt = 0
while len(circle) > 0:
    cnt += 1
    if cnt % k == 0: # k번째 일때
        result += str(circle.popleft()) + ", "
    else: # 다시 뒤에 추가
        circle.append(circle.popleft())
result = result[:-2] # 맨 마지막 ', ' 제거
result += ">"
print(result)

# 메모리 초과 코드
# while len(circle) > 0:
#     if k > len(circle):  # 남은 사람수가 k번째보다 적을 때
#         k %= len(circle)
#     result.append(circle[k - 1])  # k번째 사람 제거
#     left = circle[:k - 1]  # k번째 앞부분
#     right = circle[k:]  # k번째 뒷부분
#     right.extend(left)  # 원형으로 잇기
#     circle = right

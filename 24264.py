# https://www.acmicpc.net/problem/24264
import sys

n = int(sys.stdin.readline().strip())

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# -> n까지인 반복문 2번 중첩 -> O(n^2)의 시간복잡도

print(n**2)  # 수행횟수 : 이중반복
print(2)  # O(n^2) -> 차수 2

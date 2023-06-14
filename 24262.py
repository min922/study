# https://www.acmicpc.net/problem/24262
import sys

n = int(sys.stdin.readline().strip())

# MenOfPassion(A[], n) {
#     i = ⌊n / 2⌋;
#     return A[i]; # 코드1
# }
# -> 수행시간이 n에 depend하지 않음 O(1)의 시간복잡도

print(1)  # 수행횟수 : 반복문 없으므로 1번 수행 후 종료
print(0)  # O(1) -> 상수항은 차수 0

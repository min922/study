import sys

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

def recursion(s, l, r, cnt):
    if l >= r: return [1, cnt]
    elif s[l] != s[r]: return [0, cnt]
    else:
        cnt += 1
        return rec(s, l+1, r-1, cnt)

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

for i in data:
    print(isPalindrome(i)[0], isPalindrome(i)[1])

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

ans = max(a*b for a in range(100,1000) for b in range(100,1000) if is_palindrome(a*b))

print(ans)

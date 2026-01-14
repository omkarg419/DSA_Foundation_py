
def fect (n):
    if n <= 1:
        return 1
    else:
        return n * fect(n - 1)

print(fect(10))  # Output: 120
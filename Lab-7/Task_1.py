def factr(n):
    if n == 0:
        return 1  # Fixed: factorial of 0 is 1, not 0
    elif n == 1:
        return 1
    else:
        return n * factr(n-1)  # Fixed: should be n-1, not n-2

print(factr(5))  # Fixed: use integer 5 instead of string "5"
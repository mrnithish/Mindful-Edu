"""
Sum of digits of a number using recursion. Do it using recursion only.

Input: x = 123
Output: sum = 6

Input: x = 467
Output: sum = 17
"""
def sumOfDigits(n):
    s=0
    r=n
    while n>0:
        s=s+(n%10)
        n//=10
    return s

#Recursion
def sumOfDigitsR(n):
    s=0
    if n<=0:
        return s
    else:
        s=s+(n%10)
        return s+sumOfDigitsR(n//10)

x=467
print(sumOfDigits(x))
print(sumOfDigitsR(x))

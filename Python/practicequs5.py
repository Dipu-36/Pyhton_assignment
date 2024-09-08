def reverseDigit(n):
    while n > 0:
        r = n % 10
        print("The reverse of the number:", r)
        n = n // 10
    return 0

n = int(input("Enter the digit:"))
reverseDigit(n)

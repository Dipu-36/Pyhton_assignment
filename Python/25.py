number = input("Enter a number: ")
power = len(number)
armstrong_sum = sum(int(digit) ** power for digit in number)

if armstrong_sum == int(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

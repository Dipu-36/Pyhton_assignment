marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(4)]
average = sum(marks) / len(marks)

if average >= 75:
    grade = 'A'
elif average >= 60:
    grade = 'B'
elif average >= 40:
    grade = 'C'
else:
    grade = 'D'

print(f"Average: {average}, Grade: {grade}")

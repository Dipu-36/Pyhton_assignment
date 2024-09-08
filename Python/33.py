def generate_list_and_tuple(numbers):

  number_list = numbers.split(",")

  number_tuple = tuple(number_list)

  return (number_list, number_tuple)

numbers = input("Enter comma-separated numbers: ")

result = generate_list_and_tuple(numbers)

print(result[0])
print(result[1])
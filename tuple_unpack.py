import numbers


odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)

numbers = (*odd_numbers, *even_numbers)

print(numbers)
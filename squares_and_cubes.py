#enter range here
single_digits = list(range(10))
print(single_digits)

#prints list of squares using loop and append
squares = []
for digit in single_digits:
  squares.append(digit ** 2)
  print(digit)
print(squares)

#prints list of cubes using list comprehension
cubes = [num ** 3 for num in single_digits]
print(cubes)

# Define the factorial algorithm
def factorial(n):
  # If the number is less than or equal to 1, return 1
  if n <= 1:
    return 1
  # Otherwise, return the product of the number and the factorial of the number minus 1
  else:
    return n * factorial(n-1)

# Test the factorial algorithm
print(factorial(5)) # 120

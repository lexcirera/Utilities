def prime_factors(n):
  # Initialize the list of prime factors
  prime_factors = []

  # Divide the number by the smallest prime number (2) until it cannot be divided any further
  while n % 2 == 0:
    prime_factors.append(2)
    n = n // 2

  # Divide the number by the remaining prime numbers until it cannot be divided any further
  for i in range(3, n + 1, 2):
    while n % i == 0:
      prime_factors.append(i)
      n = n // i

  # Return the list of prime factors
  return prime_factors

# Test the prime_factors function
print("Number:" , 100, "Decomposition:" ,prime_factors(100)) # [2, 2, 5, 5]
print("Number:" , 999, "Decomposition:" ,prime_factors(999)) # [3, 3, 3, 37]
print("Number:" , 8128, "Decomposition:" ,prime_factors(8128)) # [2, 2, 2, 2, 2, 2, 2, 7, 7]

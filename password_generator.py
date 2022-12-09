import string
import random

def generate_password(length):
  # Generate a random password by choosing random characters from the letters, digits, and punctuation characters
  password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

  # Return the generated password
  return password

# Test the generate_password function
print(generate_password(8))
print(generate_password(12))
print(generate_password(16))

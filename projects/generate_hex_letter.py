import string

def generate_hex_letters():
  digits = string.digits
  alphabets_upper = string.ascii_uppercase[:6]
  alphabets_lower = string.ascii_lowercase[:6]

  hex_chars = list(digits + alphabets_upper + alphabets_lower)

  return hex_chars

print(generate_hex_letters())




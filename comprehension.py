# Data Type: Write a comprehension about yourself.

name = input("My Name: ")
# print(name)
year_of_birth = input("Year Of Birth: ")
# print(year_of_birth)
age = 2019 - int(year_of_birth)
address = input("My Home Address: ")
# print(address)

print(f"My name is {name}. "
      f"I am {age} years old. "
      f"I live at {address}.")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
random.shuffle(letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(numbers)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random.shuffle(symbols)

print("Welcome to the password generator!")
no_of_letters = int(input(f"How many letters would you like in your password?\n"))
no_of_symbols = int(input(f"How many symbols would you like in your password?\n"))
no_of_numbers = int(input(f"How many numbers would you like?\n"))

pass_list = []

for char in range(0, no_of_letters):
    pass_list.append(random.choice(letters))
for char in range(0, no_of_numbers):
    pass_list.append(random.choice(numbers))
for char in range(0, no_of_symbols):
    pass_list.append(random.choice(symbols))

random.shuffle(pass_list)
password = ''.join(pass_list)
print(f"Your password is {password}")
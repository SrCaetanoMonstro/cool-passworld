import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9',]
symbols = ['!','@','#','$','%','&','*','(','(',')','+']

print("Welcome to the PyPassworld Generator!")
nr_letters = int(input("How many letters would you like in your passworld?\n"))
nr_symbols = int(input(f"how many symbols would you like?\n"))
nr_numbers = int(input(f"how many numbers would you like?\n"))

passworld_list = []

for char in range(1, nr_letters + 1):
  passworld_list. append(random.choice(letters))

for char in range(1, nr_symbols +1):
  passworld_list += random.choice(symbols)

for char in range(1, nr_numbers +1):
  passworld_list += random.choice(numbers)

print(passworld_list)
random.shuffle(passworld_list)
print(passworld_list)

passworld = ""
for char in passworld_list:
  passworld += char

print(f"Your passworld is: {passworld}")





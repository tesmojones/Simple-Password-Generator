import random

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('1234567890') 
symbols = list('!#$%&()*+')

n_letters = int(input('how many letters? '))
n_numbers = int(input('how many numbers? '))
n_symbols = int(input('how many symbols? '))

password = []
for x in range(1, n_letters+1):
    password.append(random.choice(letters))

for x in range(1, n_numbers+1):
    password.append(random.choice(numbers))

for x in range(1, n_symbols+1):
    password.append(random.choice(symbols))
     
random.shuffle(password)
password = ''.join(password)

print(f"Your password is: {password}")
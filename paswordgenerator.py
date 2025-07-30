import random 

letters = ['a','b','c','d','e','f','g','h','i','j','k','w','r','t','u','v','y']
numbers = ['1','2','3','4','5','6','7','8','9','10']
symbols = ['!','@','#','%','&','*']

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters do you want? "))
nr_numbers = int(input("How many numbers do you want? "))
nr_symbols = int(input("How many symbols do you want? "))

password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))
    
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))
    
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)  

password = "".join(password_list)
print("Your password is:", password)

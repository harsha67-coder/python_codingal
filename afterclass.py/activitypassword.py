import random
import string

def generate_random_password(length=12):
    
    characters = string.ascii_letters 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("Your random password is:", generate_random_password(10))
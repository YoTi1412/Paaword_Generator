import random
import string

def generate_pswd(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    pswd = ''.join(random.choice(letters) for i in range(length))
    return pswd

length = int(input("Enter the lenght of the password : "))
pswd = generate_pswd(length)

# to save the password in a file 
file = input("Enter the name of the file to save the password to : ")
with open(file, 'w') as f:
    f.write(pswd)

print("Password saved to : ", file)


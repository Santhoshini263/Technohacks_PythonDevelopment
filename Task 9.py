import random
import string

# function to generate random password
def random_password_generator(pwd_choice):
    pwd_len = int(input("Enter the length of the password you need:"))
    rand_pwd = " "
    for i in range(pwd_len):
        rand_pwd += random.choice(pwd_choice)
    return rand_pwd  # returns the string

if __name__ == "__main__":
    pwd_choice = " "
    print("**********RANDOM PASSWORD GENERATOR***********")
    print("Enter your choice of password to be created")
    while True:
        opt = int(input("\n1. Uppercase letters \n2. Lowercse letters \n3. Digits \n4. Special Characters \n5. Enough \nYour choice:"))
        match opt:
            case 1:
                pwd_choice += string.ascii_uppercase
                continue
            case 2:
                pwd_choice += string.ascii_lowercase
            case 3:
                pwd_choice += string.digits
                continue
            case 4:
                pwd_choice += string.punctuation
                continue
            case 5:
                break

    pwd = random_password_generator(pwd_choice)
    print("Randomly Generated Password is :", pwd)

import string

def check_password():
    count = 0
    password = input("Input Your Password: ")
    if any(char in string.ascii_uppercase for char in password):
        count +=1
    if any(char in string.digits for char in password):
        count +=1
    if any(char in string.punctuation for char in password):
        count +=2
    return count
def main():
    strength = check_password()
    if strength ==0:
        print("Password is weak")
    elif strength ==1:
        print("Password is strong")
    elif strength ==2:
        print("Password is stronger")
    elif strength ==3:
        print("Password is very strong")

if __name__ =="__main__":
    main()
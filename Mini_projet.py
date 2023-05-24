
emails = []
passwords = []

def readFromFile():
    with open("emails_passwords.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            x = line.strip().split(' ')
            emails.append(x[0])
            passwords.append(x[1])

def validateEmail(email):
    while True:
        if '@' in email and '.':
            return True
        else:
            print("Please enter a correct email address!")
            return False
      
def signIn(email, password):
    if email in emails:
        index = emails.index(email)
        if password == passwords[index]:
            return True
    return None
readFromFile()

def getValidEmail():
    while True:
        email = input("Enter your email address: ")
        if email in emails:
            print("Email already exists!")
        elif not validateEmail(email):
            pass
        else:
            return email

import re        
def IsValidPassword(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True

def signUp(email, password):
        with open("emails_passwords.txt", "a") as f:
            f.write(f"{email} {password}\n")
        emails.append(email)
        passwords.append(password)
        print("Successfully signed up!")
        readFromFile()

def main():
    readFromFile()
    choice = input("Enter 1 to sign up, 2 to sign in: ")
    if choice == "1":
        email = input("Enter your email address: ")
        while email not in emails:
                print("Email Adress doesn't exist or not valid! please try again!")
                email = input("Enter a valid address email: ")
        password = input("Enter your password: ")
        attempts = 3
        signedin = False
        while attempts > 0 and not signedin:
            if signIn(email, password):
                print("Successfully signed in! Welcome!")
                signedin = True
                break
            else:
                attempts -= 1
                if attempts == 0:
                    print("Wrong password! Program closed!")
                else:
                    print(f"Invalid password. {attempts} attempts remaining.")
                    password = input(f"Enter your password again: ")
    elif choice == "2":
        email = getValidEmail()
        password = input("Enter your password: ")
        while not IsValidPassword(password):
           print("Invalid password. Password should be more than 8 characters and include both upper and lower case letters and numbers.")
           password = input("Enter a valid your password: ")
        signUp(email, password)                
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()        
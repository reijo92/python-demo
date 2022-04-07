"""Link for better password encryption: https://cryptography.io/en/latest/fernet -> section: Using passwords with Fernet"""
from cryptography.fernet import Fernet



'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rsplit()
            data =  data[0].split("|")
            user, passw = data[0], data[1]
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())



def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit: ").lower()
    if mode == "q":
        break


    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue


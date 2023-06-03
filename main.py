import secrets
import string
import pyperclip

def generate_special_chars(num_chars):
    special_chars = ":><?@#$%^&*()_+-=[]{}|;':\",./<>\\"
    return ''.join(secrets.choice(special_chars) for _ in range(num_chars))

def generate_letters_and_numbers(length):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_password(length, num_special_chars):
    password = generate_letters_and_numbers(length - num_special_chars)
    special_chars = generate_special_chars(num_special_chars)
    password_list = list(password)
    for char in special_chars:
        index = secrets.randbelow(length)
        password_list.insert(index, char)
    return ''.join(password_list)

def main():
    length = int(input("How long do you want your password to be?: "))
    num_special_chars = int(input("How many special characters do you want to use in your password?: "))

    password = generate_password(length, num_special_chars)
    print("Your password is:", password)

    pyperclip.copy(password)
    print("Your password has been copied to the clipboard. You can paste it using Ctrl+V.")

    input("Press Enter to exit")

if __name__ == '__main__':
    main()

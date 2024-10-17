# Peter Gardiner

def menu():
    global choice
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    choice = int(input("Please enter an option: "))

def encode(password):
    password = list(str(password))
    encoded_password = ""

    for i in range(len(password)):
        password[i] = (int(password[i]) + 3) % 10
        encoded_password += str(password[i])

    return encoded_password

def decode(encoded_password):
    password = "placeholder"
    return password

if __name__ == "__main__":
    running = True
    encoded_password = ""

    while running:
        menu()

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.\n")
        elif choice == 3:
            running = False
            exit()

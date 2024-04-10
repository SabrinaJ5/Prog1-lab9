# Sabrina Joseph

def encoder(pw):
    encoded_pw = ''
    for num in pw:
        encoded_digit = str((int(num) + 3) % 10)  # Shifting each digit up by 3
        encoded_pw += encoded_digit
    return encoded_pw

def menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

def main():
    menu()
    try:
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print(f"{password} >> {encoded_password}") # DELETE LATER
        elif option == 2:
            pass
        elif option == 3:
            exit()
    except ValueError:
        print("Unrecognized menu selection!")


if __name__ == "__main__":
    main()